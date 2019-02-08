import requests
#changer le nom, ajouter une pièce, etc…
r = requests.post("http://localhost:5000/immo/add", json={"token":"RdJkjoMmjZThofeoYMUl85PR1JgKIXcxGVHVwfdIomw", "title":"anotherrandomtitle", "nb_rooms":"666"})
print(r.status_code)
print(r.json())
