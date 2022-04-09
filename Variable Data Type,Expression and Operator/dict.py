# myprofile ={
#     "first_name":"ฉันก็ไม่รู้ฉันชื่ออะไร",
#     "last_name":"ถามสกุลก็ไม่รู้",
#     "age":112 ,
#     "tell":"02112312311",
#     "ID":"SD_123112065"
# }
# print(myprofile["first_name"],myprofile["last_name"],myprofile.get("ID"))

countries = {"de": "Germany", "ua": "Ukraine", "th": "Thailand", "nl": "Netherlands"}
print(countries.keys())
print(countries.values())

print(countries.get("de"))  # equal to countries['de']
countries.setdefault("tr", "Turkey")

print(countries.popitem())
print(countries.popitem())

print(countries.items())
