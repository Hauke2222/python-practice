my_dict = {
    "my_key": "value"
}

bands = [
    {
        "title": "band1",
        "type": "rock1"
    },
    {
        "title": "band2",
        "type": "rock2"
    }
]

band1 = list(filter(lambda band: band["title"] == "band1", bands))

print(band1[0]["type"])