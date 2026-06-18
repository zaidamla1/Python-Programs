# Ordered,unchangeable
countries= ("New Zealand","Australia","United Kingdom","Ukraine","Canada","Portugal","Netherlands","Georgia","Belgium","India")

# print(countries)
# print(type(countries))

african_countries = tuple(("Morrocow","Mauritania","Somalia", "Mauritania"))

# print(african_countries)

# print(african_countries[2])
# print(countries[1:7])
# print(countries[-1])
# print(countries[2:])
# print(countries[:3])


mylist = list(african_countries)

mylist[0]="Egypt"
print(mylist)

african_countries= tuple(mylist)
print(african_countries)

mauritania_count = african_countries.count("Mauritania")
print(mauritania_count)

somalia_pos = african_countries.index("Somalia")
print(somalia_pos)