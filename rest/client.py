import requests

def serverCalls(url,data):
    response = requests.post(url,json=data)
    print (response)
    print(response.content)

if __name__ == "__main__":
     serverCalls("http://10.71.11.180:50010/name",{"name":"iotlab","age":"17"})
