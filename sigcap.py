import requests
import json

url = "https://fts-uat.cardconnect.com/cardconnect/rest/sigcap"

headers = {
  'Authorization': 'Basic',
  'Content-Type': 'application/json'
}

payload = json.dumps({
  "merchid": "800000001530",
#   "retref": "199078056955",
#   "signature": "{{signature}}"
})


response = requests.request("PUT", url, headers=headers, data=payload)

res = response.json()
print(json.dumps(res, indent=4))
