import os

print(os.getcwd())
#r=read

#a=append
#w=WRite
#=Create

 
# Read-error if it doesn't exist

f = open("names.txt")
#print(f.read(4)) 
# print(f.readline())
# print(f.readline())
for line in f:
    print(line)
f.close()


try:
    f= open("name_list.txt")
    print(f.read())
except:
    print("the file you want to read doesnt exist")
finally:
    f.close()

#Append - creates the file if it doesn't exist
f= open("names.txt", "a")
f.write("Neil\n")
f.close()

f= open("names.txt")
print(f.read())
f.close()

#Write (overwrite)
f=open("context.txt","w")
f.write("I deleted all of context")
f.close()

f= open("context.txt")
print(f.read())
f.close()

#Two ways to create a new file
# OPens a file for writing,creates the file if it doesn't exist

f=open("name_list.txt","w")
f.close()

#creates the specified file but returns an error if the file exists
if not os.path.exists("dave.txt"):
    f=open("Dave.txt","x")
    f.close()

#Delete a file 
#avoid an error if it doesn;t exist
if os.path.exists("Dave.txt"):
    os.remove("Dave.txt")
else:
    print("the file does not exist")


with open("names.txt") as f:
    content = f.read()

with open("more_names.txt","w") as f:
    f.write(content)