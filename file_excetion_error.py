print("this is a sample.txt file")
print("it caintent multiple line")

try:
    
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())
        file.close() 
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")


user = input("Enter text to write to the file:-")
with open("output.txt","w") as file:
    file.write(user + "\n")
print("Data successfully writ output.txt")

additional = input("Enter addition text to append:-")
with open("output.txt","a") as file:
    file.write(additional + "\n")
    print("Data successfull Append output.txt")

print("Finali contetn of output.txt:")
with open("output.txt","r") as file:
    for line in file:
        print(line.strip())


