# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1
'''
Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
'''


def non_repeating_char(strng):
    alphabet_dict = {}
    for i in strng:
        if i not in alphabet_dict:
            alphabet_dict.update({i : 1})

        else:
            alphabet_dict.update({i : "repeated"})       

    print(alphabet_dict)
    for key, value in alphabet_dict.items():
        if value == 1:
            ans_key = key
            print(f"this is ans key {ans_key}")
            break
        else:
            pass
    
    print(strng.index(ans_key))


strng = "loveleetcode"
non_repeating_char(strng)

