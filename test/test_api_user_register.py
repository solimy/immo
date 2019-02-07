import requests
r = requests.post("http://localhost:5000/user/register", json={"login": "arandomlogin", "password":"arandompassword"})
print(r.status_code)
print(r.json())
