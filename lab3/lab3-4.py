def length_of_longest_substring(string):
    char_index = {}  
    max_length = 0  
    start_index = 0      

    for end_index, char in enumerate(string):
        if char in char_index and char_index[char] >= start_index:
            start_index = char_index[char] + 1
        
        char_index[char] = end_index
        max_length = max(max_length, end_index - start_index + 1)

    return max_length

input_string = "abcdefghlo"
print(length_of_longest_substring(input_string))