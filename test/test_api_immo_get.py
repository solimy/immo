import requests
r = requests.post("http://localhost:5000/immo/get", json={"token":"RdJkjoMmjZThofeoYMUl85PR1JgKIXcxGVHVwfdIomw"})
print(r.status_code)
print(r.json())
