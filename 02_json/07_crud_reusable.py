def get_all_items(items):
    return items


def find_item(items, id):
    for item in items:
        if item['id'] == id:
            return item
    return None


def update_item(items, id, updated_item):
    item = find_item(items, id)
    if item is None:
        return None
    item.update(updated_item)
    return item


def create_item(items, item):
    new_item = item.copy()
    new_item.update({'id': items[-1]['id'] + 1})
    items.append(new_item)
    return new_item


def remove_item(items, id):
    item = find_item(items, id)
    if item is not None:
        items.remove(item)
    return item
