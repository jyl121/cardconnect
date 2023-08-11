import requests
import json
import connect

url = "https://bolt-uat.cardpointe.com/api/v2/disconnect"

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'ZCb8pPkXcZDVO0CIngLSFrBJgA/BYyUZIHT8zaj3MPg=',
  'X-CardConnect-SessionKey': connect.cardConnectSessionKey
}

payload = json.dumps({
  "merchantId": "800000001530",
  "hsn": "222917393031318127346626"
})


response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)
