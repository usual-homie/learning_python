#basics of tuples operation
#they are inside braces/bracket
# they are like lists but immutable (you can't mess with them so much)

colors = ("neela","peela","lal")#wo jad arang dikha gyi aur m colorblind tha..... haso mat tumhara bhi yehi scene h

#accessing elements
print(colors[0]) #same list wala concept
print(colors[-1]) #same cheez lis wali


#looping through tuple
for c in colors:
    print(c)

#checking existence
if "neela" in colors:
    print("suno kahani ka no.1 ka roll no.21")

#modifying will give error
#color[0]= "gulabi" # error dega yeh