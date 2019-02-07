import requests
#changer le nom, ajouter une pièce, etc…
r = requests.post("http://localhost:5000/immo/add", json={"token":"thetoken", "title":"arandomtitle", "rooms":"666"})
print(r.status_code)
print(r.json())
