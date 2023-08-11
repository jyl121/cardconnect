import requests
import json
import connect 

url = "https://bolt-uat.cardpointe.com/api/v2/display"

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'ZCb8pPkXcZDVO0CIngLSFrBJgA/BYyUZIHT8zaj3MPg=',
  'X-CardConnect-SessionKey': connect.cardConnectSessionKey
}

payload = json.dumps({
  "merchantId": "800000001530",
  "hsn": "222917393031318127346626",
  # "text": "Wubba Lubba Dub Dub",
  # "text": "Jiyoon is testing Lane 5000.\n CardPointe Integrated Terminal API."
  "text": "Hello World"
})

response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)


# sends a text string, which is displayed on the idle terminal. 
# Sending a single-line string displays the text in the display footer area, retaining the idle image.
# Sending a multi-line string displays the text in the primary display area, replacing the idle image.
# to include a percent sign (%) in the display text, you must include two percent signs (%%) in the request.