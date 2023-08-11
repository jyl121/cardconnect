import requests
import json
import connect 

url = "https://bolt-uat.cardpointe.com/api/v2/dateTime"

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'ZCb8pPkXcZDVO0CIngLSFrBJgA/BYyUZIHT8zaj3MPg=',
  'X-CardConnect-SessionKey': connect.cardConnectSessionKey
}

payload = json.dumps({
  "merchantId": "800000001530",
  "hsn": "222917393031318127346626",
  "dateTime": "2023-08-07T11:30:45"
})

response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)


# A call to the dateTime endpoint sends a request to the specified terminal to set the terminal's system time.