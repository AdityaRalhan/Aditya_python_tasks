# Q1 

# def take_input():
#     lst = []
    
#     while True:
#         num = int(input("Enter the numbers, enter -1 to end input : ")) 
#         if num % 2 == 0:
#             lst.append(num)

#         elif num == -1:
#             break

#         else :
#             continue
    
#     return lst

# ans = take_input()
# print(f"List is : {ans}")

# ********************************************************************

#Q2

# def finding_consonants():
#     strng = input("Enter word ")
#     vowel = 0
#     consonant = 0
#     strng2 = strng.lower()
#     for i in strng:
#         if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#             vowel += 1
        
#         else :
#             consonant += 1

#     return vowel, consonant

# v, c = finding_consonants()
# print(f"Vowels are : {v}, consonants are : {c}")

# ********************************************************************

# Q3

# def finding_consonants():
#     strng = input("Enter sentence : ")
#     vowel = 0
#     consonant = 0
#     strng2 = strng.lower()
#     for i in strng:
#         ascii_value = ord(i)
#         if ascii_value >= ord('a') and ascii_value <= ord('z'):
#             if ascii_value == ord('a') or ascii_value == ord('e') or ascii_value == ord('i') or ascii_value == ord('o') or ascii_value == ord('u'):
#                 vowel +=1

#             else:
#                 consonant +=1
#         else:
#             continue
#     return vowel, consonant

# v, c = finding_consonants()
# print(f"Vowels are : {v}, consonants are : {c}")

# ********************************************************************

# Q4 find the longest word

# def longest_word():
#     strng = input("Enter the sentence : ")
#     words = strng.split()
#     longest_word = " "

#     for word in words:
#         if len(word) > len(longest_word):
#             longest_word = word

#     return longest_word


# ans = longest_word()
# print(f"Longest word is : {ans}")



    




# *****************************************************************
# this are other attempts.
#(IGNORE) !!

'''
def longest_word(my_input):
    i = 0
    max_length = 0
    length_string = len(my_input)
    while i< length_string:
        current_length = 0
        if ord(my_input[i]) <= ord('z') and ord(my_input[i]) >= ord('a'):
            while ord(my_input[i]) <= ord('z') and ord(my_input[i]) >= ord('a'):
                i+=1
                current_length+=1
                if (i == length_string):
                    if current_length>max_length:
                        max_length=current_length
                    break
                
                if(not (ord(my_input[i]) <= ord('z') and ord(my_input[i]) >= ord('a'))):
                    if current_length>max_length:
                        max_length=current_length
                    
                    
                   

        i+=1
    return max_length

my_input = input("Enter a sentence:")
print(longest_word(my_input))

        

def longest_word():
    strng = input("Enter the sentence : ")
    longest_word = " "
    for word1 in strng:
        for word2 in strng:
            if len(word1) > len(word2):
                longest_word = word1

            else :
                longest_word = word2
    
    return longest_word

ans = longest_word()
print(f"Longest word is : {ans}")
'''







