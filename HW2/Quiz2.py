alma_mater = "Proud and immortal Bright shines your name Oklahoma State We herald your fame Ever you'll find us Loyal and true To our Alma Mater (O-S-U)."
def get_top_chars(text):
    unique_chars = set(text)
    top_chars_list = []
    for char in unique_chars:
        count = text.count(char)
        top_chars_list.append((char, count))
    
    
    top_chars_list = sorted(top_chars_list, key=lambda x: x[1], reverse=True)
    return top_chars_list


top_chars = get_top_chars(alma_mater)
print(top_chars)

