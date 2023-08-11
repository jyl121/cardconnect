import requests
import json
import connect

url = "https://bolt-uat.cardpointe.com/api/v2/readCard"

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'ZCb8pPkXcZDVO0CIngLSFrBJgA/BYyUZIHT8zaj3MPg=',
  'X-CardConnect-SessionKey': connect.cardConnectSessionKey
}

payload = json.dumps({
  "merchantId": "800000001530",
  "hsn": "222917393031318127346626",
  "amount": "1000",
  "includeSignature": "true",
  "gzipSignature": "true",
  "signatureFormat": "png",
  "signatureImageType": "rgb",
  "signatureDimensions": "320,450",
  "includeAmountDisplay": "true",
  "confirmAmount": "true",
  "beep": "false",
  "aid": "credit"
})


response = requests.request("POST", url, headers=headers, data=payload)

res = response.json()
print(json.dumps(res, indent=4))