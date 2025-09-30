from lista import List
from JediData import jedis

# Cargamos la lista
jedi_list = List(jedis)

# a) Listado ordenado por nombre y por especie
print("\n[a] Listado ordenado por nombre:")
for jedi in sorted(jedi_list, key=lambda j: j["name"]):
    print(f" - {jedi['name']}")

print("\n[a] Listado ordenado por especie:")
for jedi in sorted(jedi_list, key=lambda j: j["species"]):
    print(f" - {jedi['name']} ({jedi['species']})")


# b) Mostrar toda la info de Ahsoka Tano y Kit Fisto
print("\n[b] Información de Ahsoka Tano y Kit Fisto:")
for jedi in jedi_list:
    if jedi["name"] in ["Ahsoka Tano", "Kit Fisto"]:
        print(jedi)


# c) Mostrar todos los padawan de Yoda y Luke Skywalker
print("\n[c] Padawans de Yoda y Luke Skywalker:")
padawans_yoda = [j["name"] for j in jedi_list if "Yoda" in j["masters"]]
padawans_luke = [j["name"] for j in jedi_list if "Luke Skywalker" in j["masters"]]
print(" - Yoda:", padawans_yoda if padawans_yoda else "Ninguno")
print(" - Luke Skywalker:", padawans_luke if padawans_luke else "Ninguno")


# d) Mostrar Jedi humanos y twi'lek
print("\n[d] Jedis humanos y twi'lek:")
for jedi in jedi_list:
    if jedi["species"].lower() in ["human", "twi'lek"]:
        print(f" - {jedi['name']} ({jedi['species']})")


# e) Listar todos los Jedi que comienzan con 'A'
print("\n[e] Jedis que comienzan con 'A':")
for jedi in jedi_list:
    if jedi["name"].startswith("A"):
        print(f" - {jedi['name']}")


# f) Jedi que usaron más de un color
print("\n[f] Jedis con más de un color de sable:")
for jedi in jedi_list:
    if len(jedi["lightsaber_colors"]) > 1:
        print(f" - {jedi['name']}: {jedi['lightsaber_colors']}")


# g) Jedi que usaron amarillo o violeta
print("\n[g] Jedis que usaron sable amarillo o violeta:")
for jedi in jedi_list:
    if "yellow" in jedi["lightsaber_colors"] or "purple" in jedi["lightsaber_colors"]:
        print(f" - {jedi['name']}: {jedi['lightsaber_colors']}")


# h) Padawans de Qui-Gon Jinn y Mace Windu
print("\n[h] Padawans de Qui-Gon Jinn y Mace Windu:")
padawans_quigon = [j["name"] for j in jedi_list if "Qui-Gon Jinn" in j["masters"]]
padawans_mace = [j["name"] for j in jedi_list if "Mace Windu" in j["masters"]]
print(" - Qui-Gon Jinn:", padawans_quigon if padawans_quigon else "Ninguno")
print(" - Mace Windu:", padawans_mace if padawans_mace else "Ninguno")
