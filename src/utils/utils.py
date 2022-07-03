import requests


def validate_redirect(url):
    req = requests.get(url)
    print(req)
    if req.status_code == 200:
        return True, req.status_code
    else:
        return False, req.status_code