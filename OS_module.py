import os
from datetime import datetime
print(dir())
print(os.getcwd())

print(os.listdir())
os.chdir('C:/Users/User/Desktop/')

os.mkdir('OS-Demo/')
os.mkdirs('OS-Demo/Sdir1/Sdir2')

os.rmdir('OS-Demo/Sdir1/Sdir')
os.removedirs('/d1') #delet the entire directory tree

os.rename('src')
os.rename('src.txt', 'target.txt')

os.stat('target.txt')
print(os.stat('target.txt').st_mtime)
mod_time = os.stat('target.txt').st_mtime)
print(datetime.fromtimestamp(mod_time))

#dir tree 
os.walk()
#traverse depth first?
for dirpath, dirname, filename in os.walk(getcwd())
    print('current path:', dirpath)
    print('current directory:', dirnames)
    print('Files:', filenames)

print(os.environ.get('HOME'))
file_path = os.environ.get('HOME'))
#trailing / os.path module
file = os.path.join(file_path, 'text.txt')

with open(file, 'w') as f:
    f.write("...")

print(os.path.dirname('/tmp/test.txt'))
print(os.path.basename('/tmp/test.txt')) #the file name
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isdir('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))

#parsing
print(os.path.splittext('/tmp/test.txt'))
#('/tmp/test', '.txt')
print(dir(os.path))
