# Q2

def finding_consonants():
    strng = input("Enter word ")
    vowel = 0
    consonant = 0
    strng2 = strng.lower()
    for i in strng:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vowel += 1
        
        else :
            consonant += 1

    return vowel, consonant

v, c = finding_consonants()
print(f"Vowels are : {v}, consonants are : {c}")