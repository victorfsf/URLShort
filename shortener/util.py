from string import digits, ascii_letters

_chars = ascii_letters + digits

def to_char(table):
    return ''.join([_chars[i] for i in table])

def to_base62(url_id):
    table = []
    
    while url_id > 0:

        mod = url_id % 62
        table.append(mod)
        url_id = int(url_id / 62)
        
    table.reverse()
    
    result = to_char(table)
    
    while len(result) < 4:
         result = 'a' + result
    
    return result

def from_base62(url_str):
    i = 0
    
    for j in url_str:
        i = i * 62 + _chars.index(j)
    
    return i