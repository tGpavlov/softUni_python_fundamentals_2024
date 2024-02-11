animal_body_parts = []

for current_body_part in range(3):
    body_part = input()
    animal_body_parts.append(body_part)

animal_body_parts[0], animal_body_parts[2] = animal_body_parts[2], animal_body_parts[0]

print(animal_body_parts)