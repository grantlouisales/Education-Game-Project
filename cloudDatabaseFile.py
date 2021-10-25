import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

"""
TODO:
    Create a class to push and receive firebase
    information.
"""
def open_data(filename):
    """
    Purpose: Reads a json and loads it into a variable.
    Return: variable holding json information.
    """
    f = open(filename)
    data = json.load(f)

    return data

db = firestore.client()
data = open_data("words.json")

# for word in data["commonWords"]:
info = {"word": data["commonWords"]}
db.collection("Words").document("Common Words").set(info)