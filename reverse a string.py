string=input("Please enter your own string:")

string2=('')
for i in string:
    string2 = i + string2

print("/n The Original String=", string)
print("/nThe Reverse String = ", string2)