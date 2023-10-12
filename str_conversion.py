def get_num_from_str(word):
    target_base = 26

    word_len = len(word)
    temp_num = 0

    for i, chr in enumerate(word):
        
        print(i , chr)
        symbol_val = ord(chr) - ord("a")
        exponent = word_len - i - 1
        temp_num += symbol_val * (target_base ** exponent)

    return temp_num

print(get_num_from_str("bbbb") > get_num_from_str("aaaa"))
print(get_num_from_str("abcd"))
print(get_num_from_str("abcbb"))

print(ord("A"))
print(ord("b"))
print(ord("@"))
print(ord("9"))