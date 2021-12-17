import requests

def skinCare(skin):
    api_address = "http://localhost:4000/products/"
    url = api_address+skin
    json_data=requests.get(url).json()
    # for data in json_data:
    #     print(data)
    return json_data
