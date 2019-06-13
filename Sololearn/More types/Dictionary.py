ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])
# print(ages["Lucy"]) KeyError

ages["Lucy"] = 25
print(ages)

print("Lucy" in ages)
print("Lea" not in ages)

print(ages.get("Gor"))
print(ages.get("Lucy"))
print(ages.get("Chris", 37))

