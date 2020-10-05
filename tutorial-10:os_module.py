import os
from datetime import datetime

#print(dir(os))
print(os.getcwd())

os.chdir('/home/kaushik')
print(os.getcwd())

os.chdir('/home/kaushik/')
os.mkdir("temp2")           # we can not create subdirectories
os.makedirs("temp3/sub2")   # can create sub directories  ---> This is more preferable

os.rmdir("temp2")           # this is more preferable.. as deleting all directories along with subdirectories are more dangerous
os.removedirs("temp3/sub2")

print(os.listdir())
os.rename('test.txt','rename.txt')
print(os.listdir())
os.rename('rename.txt','test.txt')

print(os.stat('test.txt'))
print(os.stat('test.txt').st_atime)
time = os.stat('test.txt').st_atime
print(datetime.fromtimestamp(time))

for dirpath, dirname, filename in os.walk('/home/kaushik/'):
    print('Current Path: ',dirpath)
    print('Directories:', dirname)
    print('Files:', filename)
    print()

print(os.environ.get('HOME'))
print(os.environ.keys())

filepath = os.path.join(os.environ.get('HOME'), 'Python', 'test.txt')
print(filepath)

print(os.path.basename('/tmp/tilu/test.txt'))
print(os.path.dirname('/tmp/tilu/test.txt'))
print(os.path.split('/tmp/tilu/test.txt'))
print(os.path.splitext('/tmp/tilu/test.txt'))
print(os.path.exists('/tmp/tilu/test.txt'))
print(os.path.isfile('/tmp/tilu/test.txt'))
print(os.path.isdir('/tmp/tilu/test.txt'))
