import requests
r = requests.post("http://localhost:5000/immo/list", json={"key": "value"})
print(r.status_code)
print(r.json())