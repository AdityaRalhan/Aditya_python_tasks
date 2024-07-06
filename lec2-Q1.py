# Q1 

def take_input():
    lst = []
    
    while True:
        num = int(input("Enter the numbers, enter -1 to end input : ")) 
        if num % 2 == 0:
            lst.append(num)

        elif num == -1:
            break

        else :
            continue
    
    return lst

ans = take_input()
print(f"List is : {ans}")