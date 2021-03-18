import os
import requests

token = "xapp-1-A01RVFHU5HS-1866587982598-00489a85d3ab40869088e98724548d51a08c3f392d25a1c84f1cfe115d276ce7"
file_id = "F12345678"

# call file info to get url
url = "https://slack.com/api/files.info"
r = requests.get(url, {"token": token, "file": file_id})
r.raise_for_status
response = r.json()
assert response["ok"]
file_name = response["file"]["name"]
file_url = response["file"]["url_private"]
print("Downloaded " + file_name)

# download file
r = requests.get(file_url, headers={'Authorization': 'Bearer %s' % token})
r.raise_for_status
file_data = r.content   # get binary content

# save file to disk
with open(file_name , 'w+b') as f:
  f.write(bytearray(file_data))
print("Saved " + file_name + " in current folder")
