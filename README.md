# File Handling in Python 🐍

This is a simple Python program that demonstrates basic file handling operations:

### ✅ Features:

1. **Reads from a file** named `sample.txt`.
2. **Handles errors** if the file is not found.
3. **Takes user input** and writes it to `output.txt`.
4. **Appends more data** to the same file.
5. **Displays the final content** of `output.txt`.

---

### 📄 Python Code:

```python
print("this is a sample.txt file")
print("it caintent multiple line")

try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())
        file.close() 
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

user = input("Enter text to write to the file:- ")
with open("output.txt", "w") as file:
    file.write(user + "\n")
print("Data successfully written to output.txt")

additional = input("Enter additional text to append:- ")
with open("output.txt", "a") as file:
    file.write(additional + "\n")
print("Data successfully appended to output.txt")

print("Final content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
📦 Sample Output:
vbnet
Copy
Edit
this is a sample.txt file
it caintent multiple line
Error: The file 'sample.txt' does not exist.
Enter text to write to the file:- Hello, World!
Data successfully written to output.txt
Enter additional text to append:- Welcome to Python!
Data successfully appended to output.txt
Final content of output.txt:
Hello, World!
Welcome to Python!
🚀 How to Run:
Make sure Python is installed.

Save the script as file_program.py.

Run it using:

bash
Copy
Edit
python file_program.py
📁 Files Used:
sample.txt – file to read from (create it if not present).

output.txt – file where user input is saved.

🧠 Notes:
Uses with open(...) to handle files safely.

Uses .strip() to clean line breaks when printing.

Error handling is done using try-except.

📌 Author
Created by [Your Name]

vbnet
Copy
Edit

Let me know if you want help uploading this to GitHub or want a simpler version# File-Exception-and-Error-
