filepy=open('/Users/manjunathprabhakar/FilesAndData/FilehandlingPy.txt','w') # open a file for Writing in python
filepy.write("This is my python programming file handling testing \n")
filepy.write("I love to do python programming \n")
filepy.close()

file=open('/Users/manjunathprabhakar/FilesAndData/FilehandlingPy.txt','r')
print(file.read(12))
file.close()


