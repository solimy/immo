import requests
r = requests.post("http://localhost:5000/user/edit", json={"token":"thetoken", "first_name":"arandomfirstname", "last_name":"arandomlastname", "birth_date":"yyyymmdd"})
print(r.status_code)
print(r.json())
