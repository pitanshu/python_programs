import requests
req=requests.get("https://zenodo.org/api/deposit/depositions")
print(req.status_code)
print(req.json)
ACCESS_TOKEN='ChangeMe'
req=requests.get('https://zenodo.org/api/deposit/depositions',
                 params={'access_token': ACCESS_TOKEN})

print(req.status_code)