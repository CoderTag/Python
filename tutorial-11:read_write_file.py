fd = open('test.txt','r')
#print(dir(fd))
print(fd.name,fd.mode)
fd.close() #in this we need to explicitly close the file. But in the following case file get close by itself

# as soon as we come out of with block file close
# if we read in follwing way and file size is huge we run out of memory
with open('test.txt','r') as f:
    f_contents = f.read()
    print(f_contents)

# Following read file gives weired output like include \n as well
with open('test.txt','r') as f:
    f_contents = f.readlines()
    print(f_contents)

# if we read in follwing way we have to write readline for each line.. which is not practical though we are not running out of memory
with open('test.txt','r') as f:
    f_contents = f.readline()
    print(f_contents,end='')
    print('f-pointer is at:',f.tell())            # tell where the file pointer after read
    f_contents = f.readline()
    print(f_contents,end='')
    print('f-pointer is at:',f.tell())
    f_contents = f.readline()
    print(f_contents,end='')
    print('f-pointer is at:',f.tell())

#Practical Way
print('#'*100)
print ('Practical way')
with open('test.txt','r') as f:
    for line in f:
        print(line,end='')

print('#'*100)
# Other way of reading huge file by speifying number of charecters to read at a time
print('Other way')
with open('test.txt','r') as f:
    f.seek(10)      # start reading file from a specific pointer
    charecters_to_read = 10
    contents = f.read(charecters_to_read)
    while len(contents) > 0:
        print(contents, end='')
        contents = f.read(charecters_to_read)

print('#'*100)
#copy of text file
with open('test.txt','r') as rf:
    with open('test_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)

#copy of picture file using binary mode append b with r and w..binary mode works with text also
with open('chocolate.jpg','rb') as rf:
    with open('chocolate_copy.jpg','wb') as wf:
        for line in rf:
            wf.write(line)

# Instead of copying line by line it will be more fast if we do it using chunk size
with open('chocolate.jpg','rb') as rf:
    with open('chocolate_copy2.jpg','wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
