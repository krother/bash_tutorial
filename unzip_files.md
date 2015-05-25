
# 5. Unzip files

Please go to the directory *exercise_5*. 

## 5.1. unzipping archives

Unzipping compressed files is a very basic and important task. On Unix, you often encounter WinZip archives, .tar archives, and .gz compressed files. For unpacking Win zip files, use 

    unzip <filename>

for .tar and .tar.gz files 

    tar -xf <filename>

and for .gz files,

    gunzip <filename>

The **14th and 15th character** of the solution are in a multiply wrapped archive in the *exercise_5* directory.

#### Hint
To pack a directory and everything within, you can use the command 

    tar -cf backup.tar <directory>

To subsequently compress it, use

    gzip backup.tar
