import requests
r = requests.post("http://localhost:5000/immo/add", json={"key": "value"})
print(r.status_code)
print(r.json())