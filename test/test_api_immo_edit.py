import requests
r = requests.post("http://localhost:5000/immo/edit", json={"token":"RdJkjoMmjZThofeoYMUl85PR1JgKIXcxGVHVwfdIomw", "title":"anotherrandomtitle", "nb_rooms":"66"})
print(r.status_code)
print(r.json())
