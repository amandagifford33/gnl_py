from gnl import *

filepath = 'read_this.txt'
new = 'in.txt'
#with open(filepath) as fp, open(new, 'wt') as nf:
line = Gnl(filepath, new)
line.get_next_line()
