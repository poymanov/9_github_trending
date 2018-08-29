import requests
import sys
import datetime
import json


def get_request_date():
    today = datetime.date.today()
    return today - datetime.timedelta(days=7)


def get_request_data():
    request_date = get_request_date()
    params = {'q': 'created:>={}'.format(request_date), 'sort': 'stars',
              'order': 'desc'}
    url = 'https://api.github.com/search/repositories'

    return url, params


def get_request():
    request_success_status = 200
    url, params = get_request_data()

    request = requests.get(url, params=params)

    if not request.status_code == request_success_status:
        return None

    return request


def load_data(request):
    try:
        repositories_data = json.loads(request.text)
        return repositories_data['items']
    except json.decoder.JSONDecodeError:
        return None


def output_repositories_to_console(json_data):
    count_to_output = 20

    print('Trending repositories:', '\n')
    for repository in repositories_data[:count_to_output]:
        template = ('{html_url}\nStars: {stargazers_count}\nOpen Issues: '
                    '{open_issues_count}\n').format(**repository)
        print(template)


if __name__ == '__main__':
    request = get_request()

    if not request:
        sys.exit('Failed to connect to Github')

    repositories_data = load_data(request)

    if not repositories_data:
        sys.exit('Failed to load repositories data (incorrect format)')

    output_repositories_to_console(repositories_data)
