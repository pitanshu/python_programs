import requests
r=requests.get("https//zenodo.org/api/deposit/depositions")
print(r.status_code)
print(r.json)