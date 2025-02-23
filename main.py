import os.path

from src import *

if not os.path.exists('test'):
    extract('ramdisk.cpio', "test", 'test.txt')
else:
    repack('test', 'test.txt', 'test.cpio')

