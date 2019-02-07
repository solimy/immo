import requests
r = requests.post("http://localhost:5000/user/auth", json={"login": "arandomlogin", "password":"arandompassword"})
print(r.status_code)
print(r.json())
