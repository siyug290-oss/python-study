person = {
    "name":"Siyu",
    "age": 18,
    "scores" : {"math": 95,"english": 88 },

}
print(person["name"])
print(person.get("height", "没有记录"))
print(person["scores"]["math"])
print("age" in person)
print(len(person))