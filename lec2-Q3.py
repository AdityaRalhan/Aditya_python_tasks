# Q3 find the longest word

def longest_word():
    strng = input("Enter the sentence : ")
    words = strng.split()
    longest_word = " "

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


ans = longest_word()
print(f"Longest word is : {ans}")