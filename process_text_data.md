
# 4. Process text data
Please go to the directory *exercise_4*. 

## 4.1. comparing two files
There are two different versions of a text, *foo_long.txt*, and *foo_short.txt*. To find out, how they differ, Unix provides the command

    diff <filename1> <filename2>

Of course, you can look at the text first using *more* or a text editor. The **11th character** of the solution is the first character of the third last word in the output of *diff*.

## 4.2. Sorting a text file
Unix has a small program to sort text files alphabetically. It is called by

    more <filename> | sort

The symbol '|' is called a pipe and is often used to connect Unix programs to each other. The **12th character** of the solution is the first character of the last word of the first line from the alphabetically sorted file *10000_lines.txt*.

#### Hint
To store the sorted lines in a new file, you can add an output file, like 

    more <filename> | sort > result.txt

## 4.3. Finding words in a text file
To look for specific words in a text file, the

    grep <word> <filename>

command should be used. It produces all lines from the given file that contain the given word. The *grep* command is very powerful and can handle fuzzy search patterns called Regular Expressions (not covered here). The **13th character** of the solution is the first character of the second word in a line containing *'fool'*.

#### Hint:
You can search through many files at once by including a '&#42;' in the filename.
