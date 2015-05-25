
# 1. Directories and files

## 1.1. Navigating directories
The **first character** is hidden in a file somewhere in the *exercise1* directory tree. Use the commands

    cd <directory_name>

(do not type the pointy brackets, just insert the directory name) and

    ls

to move from one directory to the next. Look through subdirectories until you find one with the name *solution_1.1* and list its contents. If you went to a wrong directory, you can go back one level by typing:

    cd ..

or to go back to the beginning:

    cd



## 1.2. Show a hidden file
Some files are not visible immediately. To see them, you need the command

    ls -a

The **second character**, is in the same directory as the first one, but in a hidden file.

## 1.3. Execute a program
Use *cd ..* to go back to the directory *exercise_1/directoryB/*. When listing its contents, you should see a program file. To find the **third character**, you need to execute the program. In Unix, this is done by typing

    ./program_name

## 1.4. Find out how big a file is

Go to the *exercise_1/directoryC/* catalog. To find **the fourth character**, you need to find out how big the text file in the directory is. This is done with the command

    ls –l

In the table the command produces, you will find the file size in bytes, the file’s owner, permissions to read and modify it, and the date/time of the last modification. When you want to obtain the fourth character, type 

    ./file_size_check

The program will ask you for a file size.

#### Hint
When typing names of directories or files, try typing the first three characters, and press *&lt;TAB&gt;*. Unix tries to guess what you are typing.
