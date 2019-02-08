import requests
r = requests.post("http://localhost:5000/user/get", json={"token":"H7BRfVTeUn9cwa5ebMWfaNtp6goNcoFtN0OACMWZ3hQ"})
print(r.status_code)
print(r.json())
