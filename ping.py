import requests
import json
import connect

url = "https://bolt-uat.cardpointe.com/api/v2/ping"

# v1, v2 important 

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

print(response.json())


# A call to the ping endpoint sends a ping command to the specified terminal. 
# The response is true if communication with the terminal is successful. 