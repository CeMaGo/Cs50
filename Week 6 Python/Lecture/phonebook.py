import csv

#version 1
# file = open("phonebook.csv", "a") 

# name = input("NAme: ")
# number = input("Number: ")

# write = csv.write(file)
# write.writerow([name,number])

# file.close()

# with open("phonebook.csv", "a") as file:

#     name = input("Name: ")
#     number = input("Number: ")

#     write = csv.write(file)
#     write.writerow([name,number])

# auto close the file, save memory only keep file open while writing..


with open("phonebook.csv", "a") as file:

    name = input("Name: ")
    number = input("Number: ")

    write = csv.DictWriter(file, filenames =[{"name", "number"}]) # {} uncertain about curly B
    write.writerow({"name":name ,"number": number})