import requests
import json

url = "https://bolt-uat.cardpointe.com/api/v2/connect"

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'ZCb8pPkXcZDVO0CIngLSFrBJgA/BYyUZIHT8zaj3MPg='
}

payload = json.dumps({
  "merchantId": "800000001530",
  "hsn": "222917393031318127346626",
  "force": "true"
})

response = requests.request("POST", url, headers=headers, data=payload)

sessionKey = response.headers.get('X-CardConnect-SessionKey')
cardConnectSessionKey = sessionKey.split(";")[0]

print(response.status_code)
# print(cardConnectSessionKey)


# IMPORTANT***
# A call to the connect endpoint establishes a session between the terminal and the terminal service.
# response returns a session key to use in subsequent requests to the terminal.