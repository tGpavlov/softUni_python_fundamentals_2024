def increase_and_decrease(pokemon):
    increased_and_decrease = [x + pokemon if pokemon >= x else x - pokemon for x in distance_to_pokemon]

    return increased_and_decrease


distance_to_pokemon = list(map(int, input().split()))
sum_removed_pokemon = 0
while distance_to_pokemon:
    pokemon_index = int(input())
    removed_pokemon = 0

    if pokemon_index < 0:
        removed_pokemon = distance_to_pokemon.pop(0)
        sum_removed_pokemon += removed_pokemon
        distance_to_pokemon.insert(0, distance_to_pokemon[-1])
        distance_to_pokemon = increase_and_decrease(removed_pokemon)
    elif pokemon_index >= len(distance_to_pokemon):
        removed_pokemon = distance_to_pokemon.pop(-1)
        sum_removed_pokemon += removed_pokemon
        distance_to_pokemon.append(distance_to_pokemon[0])
        distance_to_pokemon = increase_and_decrease(removed_pokemon)
    else:
        removed_pokemon = distance_to_pokemon.pop(pokemon_index)
        sum_removed_pokemon += removed_pokemon
        distance_to_pokemon = increase_and_decrease(removed_pokemon)

print(sum_removed_pokemon)
