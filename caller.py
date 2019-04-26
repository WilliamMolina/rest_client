import requests

def invoke(method, resource,  headers = None, body= None):
    return getattr(requests, method)(resource, data=body, headers=headers)
