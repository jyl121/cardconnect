import requests
import json
import connect

url = "https://bolt-uat.cardpointe.com/api/v2/readConfirmation"

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'ZCb8pPkXcZDVO0CIngLSFrBJgA/BYyUZIHT8zaj3MPg=',
  'X-CardConnect-SessionKey': connect.cardConnectSessionKey
}

payload = json.dumps({
  "merchantId": "800000001530",
  "hsn": "222917393031318127346626",
  "beep": "true",
  "prompt": "Please confirm:"
})

response = requests.request("POST", url, headers=headers, data=payload)

print(response.json())


# Ensure that you allow at least a 1 second delay after sending the readConfirmation command, 
# before sending a subsequent command (for example, authCard), to prevent "terminal in use" errors.