import json

def get_endpoints():
    endpoint_data = open("endpoints.json")
    endpoints = json.load(endpoint_data)
    endpoint_data.close()
    return endpoints