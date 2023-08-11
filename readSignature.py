import requests
import json
import connect

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'ZCb8pPkXcZDVO0CIngLSFrBJgA/BYyUZIHT8zaj3MPg=',
  'X-CardConnect-SessionKey': connect.cardConnectSessionKey
}

url = "https://bolt-uat.cardpointe.com/api/v2/readSignature"

payload = json.dumps({
  "merchantId": "800000001530",
  "hsn": "222917393031318127346626",
  "prompt": "Please sign:"
#   "gzipSignature" : "false",
#   "signatureFormat" : "png",  
#   "signatureImageType" : "rgb",
#   "signatureDimensions" : "320,450"
})


response = requests.request("POST", url, headers=headers, data=payload)

print(response.json())
