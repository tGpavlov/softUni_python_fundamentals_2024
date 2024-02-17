def collect(items, item):
    if item not in items:
        items.append(item)
        return items


def drop(items, item):
    if item in items:
        items.remove(item)
        return items


def combine_items(items, old_item, new_item):
    if old_item in items:
        new_item_index = items.index(old_item) + 1
        items.insert(new_item_index, new_item)
        return items


def renew(items, item):
    if item in items:
        items.remove(item)
        items.append(item)
        return items


def items_journal(items):
    while True:

        command = input().split(' - ')
        if command[0] == 'Craft!':
            break
        action = command[0]

        if action == 'Collect':
            item = command[1]
            collect(items, item)
        elif action == 'Drop':
            item = command[1]
            drop(items, item)
        elif action == 'Combine Items':
            item_1, item_2 = command[1].split(':')
            combine_items(items, item_1, item_2)
        elif action == 'Renew':
            item = command[1]
            renew(items, item)
    return items


items_in_inventory = input().split(', ')
result = items_journal(items_in_inventory)
print(*result, sep=', ')
