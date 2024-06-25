Challenges
==========

Fruit Pipes
-----------

1. Create a new directory ``fruit/``
2. Create 7 empty text files like ``apple``, ``banana`` etc.
3. Store all file names in a text file
4. List all file names that contain the letter ``a``
5. Store the names with ``a`` in a text file
6. Use ``diff`` to find all file names not containing an ``a``

The Locked Chest
----------------

1. Create a new directory ``secret_chamber/``
2. Create an empty text file ``chest`` inside it
3. Use a pipe to store the word *treasure* inside the chest file
4. Lock the chest: remove read/write permission for everybody
5. Step out of the chamber to the parent directory
6. Hide the chamber by renaming it to ``.secret_chamber/``
7. Read the contents of the chest

Hello World with Bash
---------------------

Hello with a shell script
+++++++++++++++++++++++++
1. Write a bash script ``hello.sh`` that prints ‘Hello World’
2. Execute the program with ``source hello.sh``

Hello with environment variables
++++++++++++++++++++++++++++++++

1. Store the path+filename of ``hello.sh`` in the environment variable ``HELLO``
2. Execute the program with ``source $HELLO``

Hello repeat
++++++++++++

1. Modify ``hello.sh`` to print a message given as an command-line
   argument (accessible via ``$1``)
2. Test the script with ``source hello.sh 'Hello World``
3. Write another bash script that launches ``hello.sh`` 10 times with different messages
4. Execute everything

Hello goodbye
+++++++++++++

1. Modify ``hello.sh`` to repeat the message every 10 seconds
2. Launch the script
3. Use bash commands to terminate the process
4. Launch the script 10 times
5. Use bash to terminate all 10 processes
