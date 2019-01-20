import requests
import json

class Config:
  def __init__(self, team_name, client_key, client_secret):
    self.team_name = team_name
    self.client_key = client_key
    self.client_secret = client_secret

def build_client(team_name, client_key, client_secret):
  return Config(team_name, client_key, client_secret)

def publish_event(config, event_name, payload):
  headers = {"Content-type": "application/json",
            "client_key": config.client_key,
            "client_secret": config.client_secret}

  url = 'https://{}.reactivehub.io/event/{}'.format(config.team_name, event_name)

  return requests.post(url, data=json.dumps(payload), headers=headers)