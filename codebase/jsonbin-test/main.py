import os
import requests
from dotenv import load_dotenv

load_dotenv()

XMasterKey = os.getenv("X_MASTER_KEY")
XAccessKey = os.getenv("X_ACCESS_KEY")
bin_id = os.getenv("BIN_ID")

print(XMasterKey)

url_root = "https://api.jsonbin.io/v3"
route = f"/b/{bin_id}"
headers = {
    "X-Master-Key": XMasterKey,
    "X-Access-Key": XAccessKey,
    "Content-Type": "application/json"
}
usuario = {"username": "manolita", 
           "password": "klk"}


def read_db():
    r = requests.get(url_root + route, headers=headers)
    print(r.json())


def update_db():
    r = requests.put(url_root + route, headers=headers, json=usuario)
    print(r.json())


def add_user():
    r = requests.patch(url_root + route, headers=headers, json=usuario)
    print(r.json())


read_db()
add_user()
read_db()