# Filename: longest_substring.py

def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1
            
        char_index_map[char] = right
        current_length = right - left + 1
        max_length = max(max_length, current_length)
        
    return max_length

# --- Example Usage ---
str1 = "abcabcbb"
print(f"The length of the longest substring in '{str1}' is: {length_of_longest_substring(str1)}")

str2 = "pwwkew"
print(f"The length of the longest substring in '{str2}' is: {length_of_longest_substring(str2)}")

str3 = "tmmzuxt"
print(f"The length of the longest substring in '{str3}' is: {length_of_longest_substring(str3)}")
