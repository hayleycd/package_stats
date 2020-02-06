import json
import requests

api_url_base = 'https://pypi.org/pypi/'
desired_information = []

def get_package_info(package):
    endpoint = "{0}{1}/json".format(api_url_base, package)
    
    response = requests.get(endpoint)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return "something is wrong"

def get_version_info(package, versionA, versionB):
    package_json = get_package_info(package)
    versionA_info = package_json["releases"][versionA][0]
    versionB_info = package_json["releases"][versionB][0]
    return versionA_info, versionB_info