def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item("Tea"))
print(add_item("Vada"))
