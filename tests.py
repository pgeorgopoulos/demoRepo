import time
import requests
from app import app
import os

appenv = os.getenv('APPENV')

def test_app_file():
    with app.test_client() as c:
        rv = c.get('/')
        json_data = rv.get_json()
        assert json_data["message"] == "Automation for the People", 'message does not equal "Automation for the People"'
        now = time.time()
        assert json_data["timestamp"] <= now, 'timestamp shows future time'
        assert isinstance(json_data["timestamp"], int), 'timestamp not in correct integer format'
        return 'OK'

def test_app(ipaddr):
        r = requests.get('http://' + ipaddr + ':5000/')
        assert r.status_code == 200, 'status_code not 200'
        json_data = r.json()
        assert json_data["message"] == "Automation for the People", 'message does not equal "Automation for the People"'
        now = time.time()
        assert json_data["timestamp"] <= now, 'timestamp shows future time'
        assert isinstance(json_data["timestamp"], int), 'timestamp not in correct integer format'
        return 'OK'