capitals = {country: city for (country, city) in zip(input().split(", "), input().split(", "))}

for country, capital in capitals.items():
    print(f"{country} -> {capital}")