#open a file named  "my_file.txt"
#this will create that file if it doesnt exist
file=open('my_file.txt','w')

#Write at least three lines of text to the file, including a mix of strings and numbers.
file.write("Hello PLP \n")
file.write("File Handling Assignment. \n")
file.write("The result of 2+4=6. \n")

#Enhance your script to read the contents of "my_file.txt" and display them on the console.
file=open("my_file.txt","r")
content=file.read()
print(content)

#Modify the script to open "my_file.txt" in append mode ('a').
file=open("my_file.txt","a") #opened in append mode

#append 3 additional lines
file.write("Hello World! \n")
file.write("I am currently learning Python! \n")
file.write("Programming is awesome \n")

#Implement error handling using try, except, and finally blocks to manage potential file-related exceptions (e.g., FileNotFoundError, PermissionError). 
try:
    open("my_file.txt", "r")  #opens a file in red mode
        # Read and print each line of the file
    for line in file:
        print(line.strip()) 
except FileNotFoundError:
    print("The file 'my_file.txt' does not exist.")
except PermissionError:
    print("You do not have permission to open the file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    # This block will always execute, regardless of whether an exception occurs or not
    print("File reading completed.")


