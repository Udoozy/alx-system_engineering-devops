#!/usr/bin/python3
"""
Python scrpting that uses the REST API for EMP_ID
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "user/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", contents={
        "userId": sys.argv[1]}).json()

    comp_contents = [t.get("title") for t in todos if t.get(
        "completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(comp_contents), len(todos)))
    [print("\t {}".format(i)) for i in comp_contents]
