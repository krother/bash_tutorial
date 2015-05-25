
# 6. Run useful programs

Please go to the directory *exercise_6*. 

## 6.1. Changing file access rights

Each file on Unix has separate permissions for reading *'r'*, writing *'w'*, and executing *'x'*. When displaying them with 

    ls -l

there is one triplet of these permissions for the files owner, one for a group of users, and one for all others. The *chmod* command allows to change these permissions, e.g.

    chmod a+x <filename>

grants all users the permission to execute a file, while *u-w* forbids the current user (oneself) to write to the file (thereby protecting it from being deleted accidentally). The **next two characters** of the solution will be shown when you execute the program

    ./check_permissions

#### Hint:
You can grant permissions for a whole directory tree using

    chmod -R a+x <directory>'.

## 6.2. How much disk space have I left?
To find out, how much disk space you have left, you can use the command

    df

It lists all hard disk partitions, CD-ROMs, pendrives etc. Your data is stored in */home/*, if it does not exist, in */*. All numbers are given in kilobyte (1000 byte or one 1000000th GB).
To obtain the **18th character**, run the program

    ./check_disk

## 6.3. Set an environment variable

To install some programs, it is necessary to set so-called environment variables. These can be set using the command 

    export <variable-name>=<value>

But then the variable will only be present in the same console window where you typed the command. You can see all variables by the command

    env

To obtain the **19th character**, you need to set the variable *SOLUTION* to the value *6.3*, and run the program 

    ./check_variable

#### Hint:
If you want to have an environment variable to be automatically set for eachconsole window, write the export command to the file 
*.bashrc* in your home directory (it is a hidden file).

#### Hint: 
The *env* command can be combined nicely with *grep*, e.g. to check your PATH variable, you can type: 

    env | grep PATH


## 6.4. Check whether you have internet
The easiest way to check from the Unix command line whether the internet connection works, is to send a request to a known server (e.g. www.academis.eu) using the command

    ping <web address>

The command reports, how long a message takes back and forth to the given server. To interrupt the messages, press *Ctrl+C*. You can use the program 

    ./check_ping

to get the **20th character**.

## 6.5. Managing processes
To see what programs are running on your machine, type 

    top

It displays you a list of all currently active programs. *Shift+P* sorts them by the CPU time they are using, *Shift+M* by the amount of memory they are using (if you don't see any program consuming lots of memory, start a web browser).

The **last two characters** of the solution are the first two characters of the second word in the highlighted bar containing the column labels.

#### Hint:
If you want to get rid of one of the programs you started (e.g. because it crashed), you can do so by typing

    kill <pid>

You find the pid number in the first column of the *top* output. Of course, you may only interrupt your own programs, not those owned by *root*, the system administrator.
