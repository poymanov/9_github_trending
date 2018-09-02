import requests
import sys
import datetime
import json


def get_api_url():
    return 'https://api.github.com'


def get_request_params(period_days=7):
    request_date = datetime.date.today() - datetime.timedelta(period_days)

    params = {}
    params['q'] = 'created:>={}'.format(request_date)
    params['sort'] = 'stars'
    params['order'] = 'desc'

    api_url = get_api_url()
    request_url = '{}/search/repositories'.format(api_url)

    return request_url, params


def get_repositories_list(request_params):
    request_url, params = request_params
    response = requests.get(request_url, params=params)

    if not response.ok:
        return None

    return response.json()['items']


def get_open_issues_count(full_name):
    api_url = get_api_url()
    request_url = '{}/repos/{}/issues'.format(api_url, full_name)
    response = requests.get(request_url)

    if not response.ok:
        return 'N/A'

    open_issues_count = 0

    for issue in response.json():
        if issue['state'] == 'open':
            open_issues_count += 1

    return open_issues_count


def output_repositories_to_console(repositories_info):
    print('Trending repositories:', '\n')
    for repository in repositories_info:
        template = ('{html_url}\nStars: {stargazers_count}\nOpen Issues: '
                    '{open_issues_from_api}\n').format(**repository)
        print(template)


def get_additional_info(repositories_list):
    repositories_info = []
    repositories_count = 20

    repositories_list = repositories_list[:repositories_count]

    for repo in repositories_list:
        repo['open_issues_from_api'] = get_open_issues_count(repo['full_name'])

    return repositories_list


if __name__ == '__main__':
    request_params = get_request_params()

    repositories_list = get_repositories_list(request_params)

    if not repositories_list:
        sys.exit('Failed to connect to Github')

    repositories_info = get_additional_info(repositories_list)

    output_repositories_to_console(repositories_info)
