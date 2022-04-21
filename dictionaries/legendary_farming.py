key_materials = {'shards': "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
materials = {"shards": 0, "fragments": 0, "motes": 0}
farming = True
while farming:
    input_line = input().split(' ')
    data = iter(input_line)

    for element in data:
        quantity = int(element)
        material = next(data).lower()

        if material not in materials:
            materials[material] = quantity
        else:
            materials[material] += quantity

        if materials[material] >= 250 and material in key_materials:
            materials[material] -= 250
            print(f"{key_materials[material]} obtained!")
            farming = False
            break

for material in key_materials:
    print(f"{material}: {materials[material]}")

for material in materials:
    if material not in key_materials:
        print(f"{material}: {materials[material]}")
