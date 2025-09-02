text = input("enter text to write to the file: ")
with open('OUTPUT.txt', 'w') as file1:
    file1.write(text)
print("data successfully written to OUTPUT.txt.")

text_append = input("enter additional text to append: ")
with open("OUTPUT.TXT",'a') as file1:
    file1.write(text_append)
print("Data successfully appended.")


print("Final content of OUTPUT.txt: ")
with open('OUTPUT.TXT','r') as file1:
   reading_file =  file1.read()
   print(reading_file)
