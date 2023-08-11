import requests
import json
import connect

url = "https://bolt-uat.cardpointe.com/api/v2/readInput"

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'ZCb8pPkXcZDVO0CIngLSFrBJgA/BYyUZIHT8zaj3MPg=',
  'X-CardConnect-SessionKey': connect.cardConnectSessionKey
}

payload = json.dumps({
  "merchantId": "800000001530",
  "hsn": "222917393031318127346626",
  "prompt": "Phone number:",
  "beep": "false",
  "format": "PHONE"
#   "format" can be PHONE, AMOUNT, MMYY, N5 (zip code), N5,9, AN5, AN1,20 (DL#)
})


response = requests.request("POST", url, headers=headers, data=payload)

print(response.json())
