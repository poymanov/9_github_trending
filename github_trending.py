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


def get_response():
    request_url, params = get_request_params()

    response = requests.get(request_url, params=params)

    if not response.status_code == requests.codes.ok:
        return None

    return response


def get_open_issues(full_name):
    api_url = get_api_url()
    request_url = '{}/repos/{}/issues'.format(api_url, full_name)
    response = requests.get(request_url)

    if not response.status_code == requests.codes.ok:
        return 'N/A'

    open_issues_count = 0

    for issue in response.json():
        if issue['state'] == 'open':
            open_issues_count += 1

    return open_issues_count


def output_repositories_to_console(repositories_info):
    print('Trending repositories:', '\n')
    for repository in repositories_info:
        template = ('{url}\nStars: {stars}\nOpen Issues: '
                    '{open_issues}\n').format(**repository)
        print(template)


def get_repositories_info(repositories_data):
    repositories_list = repositories_data['items']
    repositories_info = []
    repositories_count = 20

    for repo in repositories_list[:repositories_count]:
        repo_data = {}
        repo_data['url'] = repo['html_url']
        repo_data['stars'] = repo['stargazers_count']
        repo_data['open_issues'] = get_open_issues(repo['full_name'])
        repositories_info.append(repo_data)

    return repositories_info


if __name__ == '__main__':
    response = get_response()

    if not response:
        sys.exit('Failed to connect to Github')

    repositories_info = get_repositories_info(response.json())

    output_repositories_to_console(repositories_info)
