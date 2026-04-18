def report(items):
    total = len(items)
    found = sum(1 for i in items if i['status']=='Found')
    print('Total Items:', total)
    print('Found Items:', found)
