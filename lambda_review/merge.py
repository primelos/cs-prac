def merge_packages(items, limit):
    cache = {}
    index = 0
    length = len(items)
    while index < length:
        if limit - items[index] not in cache:
            cache[items[index]] = index
            print(cache)
            index += 1
        
        else:
            return [index, cache[limit - items[index]]]

    return []

print(merge_packages([4, 6, 10, 15, 16], 21))