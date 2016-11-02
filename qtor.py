#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import json


def load_client_information(filename):
    try:
        with open(filename, "rt") as fin:
            client_informatin = json.load(fin)
    except FileNotFoundError as err:
        print(err)
        sys.exit()

    return client_informatin


def get_access_token(client_informatin):
    if not "client_id" in client_informatin:
        print("\"client_id\" is not defined in config file.")
        sys.exit()

    if not "client_secret" in client_informatin:
        print("\"client_secret\" is not defined in config file.")
        sys.exit()

    payload = {
        "client_id": client_informatin["client_id"],
        "client_secret": client_informatin["client_secret"],
        "scope": "http://api.microsofttranslator.com",
        "grant_type": "client_credentials"
    }

    schema = "https"
    host = "datamarket.accesscontrol.windows.net"
    path = "/v2/OAuth2-13"
    url = schema + "://" + host + path

    response = requests.post(url, data=payload).json()
    if "error" in response:
        print("Failed to get access token")
        sys.exit()

    access_token = response["access_token"]

    return access_token


def translate(access_token, text):
    params = {
        "text": text.encode("utf8"),
        "from": "ja",
        "to": "en",
        "contentType": "text/plain",
        "category": "general"
    }

    schema = "http"
    host = "api.microsofttranslator.com"
    path = "/v2/Ajax.svc/Translate"
    url = schema + "://" + host + path
    headers = {
        "Authorization": "Bearer %s" % access_token
    }

    response = requests.get(url, params=params, headers=headers)
    response.encoding = "UTF-8-sig"
    translated_text = response.json()

    return translated_text


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\"text\" you want to translate is required.")
        sys.exit()

    client_informatin = load_client_information("config.json")
    access_token = get_access_token(client_informatin)

    text = sys.argv[1]
    translated_text = translate(access_token, text)
    print(translated_text)
