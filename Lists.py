# Ordered, Duplicates allowed, changeable
capitals = ["New Delhi","Washington DC", "Canberra","Paris","Tokyo"]

# print(capitals)
# print(capitals[2])

# capitals[1] = "Pyangyong"
# print(capitals)

# print(capitals[1:4])
# print(capitals[-1])
# print(capitals[2:])
# print(capitals[:3])

europe_capitals=["Oslo","Ryejawick","Moscow"]
asian_capitals=["Ulanbatar", "Beijing", "Astana", "Beijing", "Islamabad", "Kabul", "Beijing","Kathmandu", "Dhaka", "Baghdad"]

europe_capitals.append("Warshaw")
# print(europe_capitals)

europe_capitals.extend(["Berlin", "Prague"])
europe_capitals.insert(3,"Ankara")
print(europe_capitals)

beijingPos = asian_capitals.index("Beijing",4,9)
print(beijingPos)

popElm = asian_capitals.pop(2)
print(popElm)
print(asian_capitals)

beijingCount = asian_capitals.count("Beijing")
print(beijingCount)

europe_capitals.remove("Ryejawick")
print(europe_capitals)

europe_capitals.reverse()
print(europe_capitals)

copied_asian_capitals = asian_capitals.copy()

copied_asian_capitals.clear()
print(copied_asian_capitals)

del copied_asian_capitals