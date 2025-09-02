'''
try:
    file1 = open('sample.txt', 'r')
    print("reading file content:")
    reading_file = file1.read()
    print(reading_file)
    file1.close()
except FileNotFoundError:
    print("Error: the file 'sample.txt' not found.")

'''
try:
    with open('sample.txt','r') as file1:
        print("Reading Line Content:")
        line_number = 1
        for line in file1:
            print(f"Line {line_number}: {line}")
            line_number += 1
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
