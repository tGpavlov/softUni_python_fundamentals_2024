# notes = [0] * 10
#
# while True:
#     command = input()
#     if command == 'End':
#         break
#
#     tokens = command.split('-')
#     priority = int(tokens[0]) - 1
#     note = tokens[1]
#     notes.pop(priority)
#     notes.insert(priority, note)
#
# result = [element for element in notes if element != 0]
# print(result)

# ========  Mario Solution =========

def process_to_do_notes():
    to_do_notes = []

    while True:
        note = input()

        if note == 'End':
            break

        to_do_notes.append(note)

    sorted_notes = sorted(to_do_notes, key=lambda x: int(x.split('-')[0]))
    sorted_notes = [note.split('-')[1] for note in sorted_notes]

    return sorted_notes


result = process_to_do_notes()
print(result)