def find_item(items, iid):
    for i in items:
        if i['id'] == iid:
            return i
    return None
