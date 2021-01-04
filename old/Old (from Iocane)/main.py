 import LSMtools
import board
import supervisor
import time
import touchio
import storage

storage.remount("/", 0)

f=open("test.txt", 'w')
f.write("Hello World!")
f.close()
