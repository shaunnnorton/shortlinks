import requests
from src import db
from src.models import LinkModel


def validate_redirect(url):
    req = requests.get(url)
    print(req)
    if req.status_code == 200:
        return True, req.status_code
    else:
        return False, req.status_code


def remove_relation(shortlink):
    LinkModel.query.filter_by(shortlink=shortlink).delete()
    db.session.commit()