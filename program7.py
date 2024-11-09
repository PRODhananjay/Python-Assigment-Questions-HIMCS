# Program to sort the sentence in alphabetical order 

a = "Harry Potter and the Goblet of Fire"

w = a.split()
for i in range (len(w)):
    w[i] = w[i].lower()

print("String be fore sort :",w)

w.sort()
print("String after sort :",w)