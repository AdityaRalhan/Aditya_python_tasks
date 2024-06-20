# create a program

#Computers ={
#  "Laptop1" : {"brand" : "DELL","OS" : "Windows"},
#  "Laptop2" : {"brand" : "HP", "OS" : "Linux"},
#  "Desktop" : {"brand" : "Apple","OS" : "Mac-OS"}
# }
# from this above data create a list brand,OS
#print(brand)
#['brand','hp','apple']
#print(os)
#['Windows','Linux','MAc-os']

Computers = {
 "Laptop1" : {"brand" : "DELL", "OS" : "Windows"},
 "Laptop2" : {"brand" : "HP", "OS" : "Linux"},
 "Desktop" : {"brand" : "Apple", "OS" : "Mac-OS"}
}

brand = []
os = []

brand.append(Computers["Laptop1"]["brand"])
brand.append(Computers["Laptop2"]["brand"])
brand.append(Computers["Desktop"]["brand"])

os.append(Computers["Laptop1"]["OS"])
os.append(Computers["Laptop2"]["OS"])
os.append(Computers["Desktop"]["OS"])

print(brand)
print(os)