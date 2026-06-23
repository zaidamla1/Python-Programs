#Duplicates not alowed, random order
countries = {"Samoa", "Kiribati", "Nauru", "Soloman Islands", "Tuvalu"}


countries.add("Papua New Guniea")
print(countries)


countries.remove("Samoa")

countries.pop()

countries.discard("Fiji")
print(countries)


asian_countries = {"India", "Pakistan", "Nepal", "Iraq"}
african_countries = {"Egypt", "Morocoow", "Algeria", "Iraq"}


fav_countries = asian_countries.union(african_countries)
print(fav_countries)


european_countries = {"Portugal","Germany","France", "United Kingdom", "Bosnia and Herzegovina"}
south_american_countries = {"Argentina","Brazil","United Kingdom", "Bosnia and Herzegovina","Uruguay"}

football = european_countries.intersection(south_american_countries)
print(football)


african_countries.intersection_update(asian_countries)
print(african_countries)