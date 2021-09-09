def add(x, y):
    return( x + y)

print(add(3, 1))

def search(term, search_str):
    if term in search_str:
        return "found"
    else:
        return "not found"

print(search('test', 'test123'))