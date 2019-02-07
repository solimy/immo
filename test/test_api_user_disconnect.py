import requests
r = requests.post("http://localhost:5000/user/disconnect", json={"token":"9yCwNZpTneWGdkJ53_aC1bfvdlgkYgcCscWJO_lo-fs"})
print(r.status_code)
print(r.json())
