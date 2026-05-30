#2 Print the content of a directory using OS MODULE 

import os #2 os Library 

# SPECIFY DIRECTORY  
directory_path='/'

#List  all files and directories in specified path 

abj=os.listdir(directory_path)

#print file in directory 

for item in abj: 
    print(item)


"""
No — this code does not always open the C drive.
It depends on the operating system and the path you write.

In your code:
directory_path = '/'

On Linux / Mac:

'/' means the root directory (top level directory).
So it will list things like:

bin
etc
home
usr
var

On Windows:

'/' usually refers to the current drive root, most commonly C:/ if your Python is running from the C drive.
So it may appear as if it is always showing C:\, but that’s only because Python is running on the C drive.

If you want to **explicitly list C:**:
directory_path = 'C:\\'

If you want to list another folder, like Desktop:
directory_path = 'C:\\Users\\YourName\\Desktop'

Summary
Path	Meaning on Windows	Meaning on Linux/Mac
'/'	Root of current drive (often C:\)	System root /
'C:\\'	Specifically C drive	Not valid on Linux/Mac

So your code does not always open C — it opens the root directory of the system, which happens to be C on most Windows setups



"""