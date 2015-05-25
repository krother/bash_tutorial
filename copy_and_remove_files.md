
# 3. Copy and remove files
Please go to the directory *exercise_3*.

## 3.1. Create a directory and copy a file to it.

To find **characters seven and eight**, you need to create a subdirectory named *solution* in *exercise_3/* and copy the file *code.txt* to it. For creating directories, you can use the command 

    mkdir <directory name>

For copying, you can use the command 

    cp <filename from> <filename to>

Use *ls solution/* afterwards to see whether the file is there. The program 

    ./check_code

will give you the solution.

## 3.2. Removing files

In the same directory, there is a file *junk.txt* that does not contain anything useful, and should be deleted. To do so, use the command

    rm <filename>

Also, there are more files to be deleted in the *data* directory. To remove more than one file at once, you can use '&#42;' as a wildcard, i.e. 'rm pro&#42;' will delete all of *profile, 'protein.txt and prototype.doc*. To get **characters nine and ten**, please run the program 

    ./check_junk

after removing the files.

#### WARNING
On Unix, it is not possible to undelete files!

#### Hint
To remove an empty directory, you can use 

    rmdir <directory name>

To delete a directory and everything in it, the command *rm -r <directory name>* exists. In combination with the '&#42;' symbol, this is dangerous, because it gives you the possibility to wipe out all your data with a single command (e.g. if you type the wrong directory by accident). Thus, first make a backup and then play with this command.
