import json
import random


def get_easy_words():
    with open("words.json", "r") as f:
        data = json.load(f)

        return data["easyWords"]


def get_medium_words():
    with open("words.json", "r") as f:
        data = json.load(f)

        return data["mediumWords"]


def get_hard_words():
    with open("words.json", "r") as f:
        data = json.load(f)

        return data["hardWords"]
        