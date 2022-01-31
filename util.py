import os, discord, json

def load_secrets():
    f = open('secrets.json')

    file = json.load(f)

    return file
