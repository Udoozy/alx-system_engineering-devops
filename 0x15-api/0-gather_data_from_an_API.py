#!/usr/bin/python3
"""
Python scrpting that uses the REST API for EMP_ID
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        user = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        content = requests.get("{}user/{}".format(url, user))
        name = content.json().get("name")
        if name is not None:
            jcontent = requests.get(
                    "{}todos?userId={}".format(
                        url, user)).json()
            all_content = len(jcontent)
            comp_content = []
            for i in jcontent:
                if i.get("completed") is True:
                    comp_content.append(i)
            count = len(comp_content)
            print("Employee {} is done with tasks({}/{}):"
                    .format(name, count, all_content))
            for Title in comp_content:
                print("\t {}".format(Title.get("Tittle")))
