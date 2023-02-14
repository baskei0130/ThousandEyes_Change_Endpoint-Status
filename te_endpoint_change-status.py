from urllib.request import urlopen, Request
from const import *
import json
import datetime
import os
import time

# HTTP GET
def http_get(request):
  with urlopen(request) as response:
    body = response.read()
  return body

# HTTP POST
def http_post(request, data):
  with urlopen(request, data) as response:
    body = response.read()
    time.sleep(3) # To wait for reflecting the API
  return body

# Get the list of Endpoint Agents
def get_endpoint_agents_list():
  request = Request(url_agents_list, headers=headers)

  # Create a file to write the list of Endpoint Agents
  dt_now = datetime.datetime.now()
  file_name = 'te_endpoint-agent_list' + dt_now.isoformat() + '.json'
  file_write = open(file_name, 'w')
  # Write the list of Endpoint Agents to the created file
  file_write.write(http_get(request).decode('utf-8'))
  file_write.close()

  # Open the created file to read the list of Endpoint Agents
  file_read = open(file_name, 'r')
  agents = json.load(file_read)['endpointAgents']
  print("\n\n{:40} {:30} {:8}".format('Agent ID', 'Agent Name', 'License Status'))
  for agent in agents:
    print("{:40} {:30} {:8}".format(agent['agentId'], agent['agentName'], agent['status']))
  # os.remove(file_name) # If you don't want to save the list on your local computer, uncomment this line.
  file_read.close()
  return agents

# Change the Endpoint Agent's status to enabled
def enable_agent(id):
  print("Change the Status of {:36} to enabled".format(id))
  request = Request(url_agent_enable + id + "/enable.json", headers=headers)
  http_post(request, data)

# Change the Endpoint Agent's status to disabled
def disable_agent(id):
  print("Change the Status of {:36} to disabled".format(id))
  request = Request(url_agent_enable + id + "/disable.json", headers=headers)
  http_post(request, data)


# main function
if __name__ == "__main__":
  while (1):
    # Get list of Endpoint Agents
    agents = get_endpoint_agents_list()
    endpoint_id = input("\nInput the ID of Endpoint Agent whose status you change (Input 0, if you quit): ")
    if endpoint_id == "0":
      break # quit program
    for agent in agents:
      if agent['agentId'] == endpoint_id:
        if agent['status'] == 'enabled':
          disable_agent(endpoint_id)
        elif agent['status'] == 'disabled':
          enable_agent(endpoint_id)
        continue