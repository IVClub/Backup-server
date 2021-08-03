import requests

server_addrs = "http://127.0.0.1:5000/upload"

filename = "/Users/xuanhuaz/Desktop/kitten.png"
data = {'file': open(filename, 'rb')}

getdata = requests.post(server_addrs, files=data)

print(getdata.text)



