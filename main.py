import requests

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

  url = 'https://{}.reactiveuh.io/event/{}`'.format(config.team_name, event_name)
  print(url)

  requests.post(url, data=payload, headers=headers)


config = build_client('reactivehub', 'eaab5f13-13b7-4a91-b7c9-d4dbc9a7c276', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lc3BhY2UiOiJyZWFjdGl2ZWh1YiIsImlkIjoiYmMyMWNkMTAtNzYxNi0xMWU4LThhOGMtZDliZjk2YzhiOGEyIiwia2V5IjoiZWFhYjVmMTMtMTNiNy00YTkxLWI3YzktZDRkYmM5YTdjMjc2IiwiaWF0IjoxNTI5NjcwMDY1fQ.Q-JUfXFcVMLnW8h-L6UqYtjOogp-jLeziuEjtjFuYEA')
publish_event(config, 'new-user', {
	"email": "luiz@reactivehub.io",
	"name": "Luiz",
	"description": "Teste python",
	"namespace": "reactivehub"
})