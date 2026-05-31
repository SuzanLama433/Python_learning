'''
      ====================File handling ======================

File : collection of data or information  to store permanently

type of file : 
text file  : store in the form of character : .py,txt,csv,html
binary file : store in the form of byte : .png,doc,pdf

File handling : 
python perform some function such as remove,append,write and read on file 

step 1: 
open the file
step 2:
perform on that file 
step3 : 
close file


stynax :

object=open(file_name,mode)

mode : 
x -->create file
r-->read the file 
w -->write on the file  
a -->append
r+ -->read and write
w+ -->write and read
a+ -->write or append and read
'''

# f=open("FileHandling/msg.txt",'a+')
# print(f.read())
# print(f.read(10))
# print(f.readline())
# print(f.readlines()) # it stored in list 
# f.write("\nsipalaya info tech\n")
# f.write("sujan")
# v=f.readlines()
# for i in v:
#     print(i)
   
#     print("-"*70)

# print(f.read())
# f.write("sujan")
#f.close()
# main problem if not close file 
# 1.data corrupted
# 2.memory wasted

#with statement
#do not need to closed file by developer

# with open("FileHandling/msg.txt",'r') as f:
#       print(f.read())

f= open("Filehandling/msg.txt",'r')
print(f.read(5))
f.seek(0)
print(f.tell())
print(f.read(6))


f.close()
# import os 
# os.remove("msg.txt") 
