# File Operations in Python - README

This repository contains Python programs demonstrating basic file operations including reading, writing, appending, and error handling.

## Problem 1: File Write, Append, and Read Operations

### Problem Statement
Write a Python program that:
1. Takes user input and writes it to a file named output.txt
2. Appends additional data to the same file
3. Reads and displays the final content of the file

### Solution
```python
# Get initial text from user and write to file
text = input("Enter text to write to the file: ")
with open('output.txt', 'w') as file:
    file.write(text)
print("Data successfully written to output.txt.")

# Get additional text and append to the same file
text_append = input("Enter additional text to append: ")
with open('output.txt', 'a') as file:
    file.write(text_append)
print("Data successfully appended.")

# Read and display the final content
print("Final content of output.txt:")
with open('output.txt', 'r') as file:
    content = file.read()
    print(content)
```

### Expected Output
```
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file handling in Python.
```

### Key Features
- Uses `with` statement for proper file handling
- Demonstrates writing (`'w'`) and appending (`'a'`) modes
- Reads and displays complete file content
- Proper resource management with automatic file closing

---

## Problem 2: File Reading with Error Handling

### Problem Statement
Write a Python program that:
1. Opens and reads a text file named sample.txt
2. Prints its content line by line
3. Handles errors gracefully if the file does not exist

### Solution
```python
try:
    with open('sample.txt', 'r') as file:
        print("Reading file content:")
        line_number = 1
        for line in file:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
```

### Expected Output

**If the file exists:**
```
Reading file content:
Line 1: This is a sample text file.
Line 2: It contains multiple lines.
```

**If the file does not exist:**
```
Error: The file 'sample.txt' was not found.
```

### Key Features
- Uses `try-except` block for error handling
- Reads file line by line using iteration
- Uses `strip()` to remove trailing newline characters
- Provides user-friendly error messages
- Demonstrates proper exception handling with `FileNotFoundError`

---

## File Operations Summary

### File Modes
- `'r'` - Read mode (default)
- `'w'` - Write mode (overwrites existing content)
- `'a'` - Append mode (adds to existing content)
- `'x'` - Exclusive creation mode (fails if file exists)

### Best Practices
1. **Always use `with` statement** - Ensures proper file closing even if errors occur
2. **Handle exceptions** - Use try-except blocks for file operations
3. **Use appropriate file modes** - Choose the right mode for your operation
4. **Strip whitespace** - Use `strip()` when reading lines to remove unwanted characters
5. **Provide user feedback** - Inform users about operation success/failure

### Common File Exceptions
- `FileNotFoundError` - File doesn't exist when trying to read
- `PermissionError` - Insufficient permissions to access file
- `IsADirectoryError` - Trying to open a directory as a file
- `OSError` - General operating system related errors

### Usage Tips
- Test your file operations with both existing and non-existing files
- Always validate file paths and names
- Consider using relative vs absolute paths based on your needs
- Remember that file operations can be platform-specific (Windows vs Linux/Mac)
