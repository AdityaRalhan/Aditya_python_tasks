# Q6)
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

#Each letter in magazine can only be used once in ransomNote.

'''
Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''

randsomeNote = "a"
magazine = "b"

def constructing(randsomeNote, magazine):
    set_randsomeNote = sorted(set(randsomeNote))
    set_magazine = sorted(set(magazine))
    print(set_randsomeNote)
    print(set_magazine)
    while (len(set_randsomeNote) > 0):
        for i in set_randsomeNote:
            if i in set_magazine:
                set_randsomeNote.remove(i)

            else : 
                print("Cannot be constructed")
                return
            
            
    print("can be constructed")

constructing(randsomeNote, magazine)

