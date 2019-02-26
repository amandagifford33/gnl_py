filepath = 'read_this.txt'
with open(filepath, 'r') as fp, open("in.txt", 'wt') as nf:
    line = fp.readline()
    nf.write(line.strip())
    count = 1
    while line:
        print("Line {} : {}".format(count, line.strip()))
        line = fp.readline()
        nf.write(line.strip())
        count += 1




#filepath = 'read_this.txt'
#with open(filepath) as fd:
 #   for count, line in enumerate(fd):
  #      print('File {}: {}'.format(count, line))
