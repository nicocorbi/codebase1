import requests

r = requests.get('https://dummyjson.com/users')
users = r.json()
#users.get
print(users.keys())

lista_users = users.get("users")
#print(lista_users)
primer_usuario = lista_users[0]
print(primer_usuario.keys())
print(primer_usuario.get("username"))
print(primer_usuario.get("password"))
