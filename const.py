import base64
from urllib.parse import urlencode

### Enter the following config
email = "" # Enter Email between double quotation
auth_token = "" # Enter Basic Authentication Token between double quotation
###

### Don't need to change anything
url_agents_list = "https://api.thousandeyes.com/v6/endpoint-agents.json"
url_agent_enable = "https://api.thousandeyes.com/v6/endpoint-agents/" # + {agent_id} + /enable
url_agent_disable = "https://api.thousandeyes.com/v6/endpoint-agents/" # + {agent_id} + /disable

basic_user_and_pass = base64.b64encode('{}:{}'.format(email, auth_token).encode('utf-8'))

headers = {
  "Authorization": "Basic " + basic_user_and_pass.decode('utf-8')
}

data = {
}
data = urlencode(data).encode("utf-8")