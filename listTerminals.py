import requests
import json

url = "https://bolt-uat.cardpointe.com/api/v2/listTerminals"

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'ZCb8pPkXcZDVO0CIngLSFrBJgA/BYyUZIHT8zaj3MPg='
}

payload = json.dumps({
  "merchantId": "800000001530"
})

response = requests.post(url, headers=headers, data=payload)

# print(response.json())

res = response.json()
print(json.dumps(res, indent=4))


# returns an array of Hardware Serial Numbers (HSNs) for each terminal for the specified merchant ID.