import requests
import json

url = "https://bolt-uat.cardpointe.com/api/v3/terminalDetails"

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'ZCb8pPkXcZDVO0CIngLSFrBJgA/BYyUZIHT8zaj3MPg=',
}

payload = json.dumps({
  "merchantId": "800000001530"
}, indent=4)

response = requests.request("POST", url, headers=headers, data=payload)

res = response.json()
print(json.dumps(res, indent=4))

# returns an array of terminals associated with the merchant ID specified in the request.