import requests
r = requests.post("http://localhost:5000/user/edit", json={"token":"RdJkjoMmjZThofeoYMUl85PR1JgKIXcxGVHVwfdIomw", "first_name":"arandomfirstname", "last_name":"arandomlastname", "birth_date":"19940321"})
print(r.status_code)
print(r.json())
