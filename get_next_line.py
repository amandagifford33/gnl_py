filepath = 'read_this.txt'
new = 'in.txt'
with open(filepath, 'r') as fp, open(new, 'w+') as nf:
    print(fp, nf)
    line = fp.readline().strip()
    print(line)
    #while (len(fp.read()) and (not line)):
        #print(line)
       # line = fp.readline().strip()
    
    #print("I made it into else")
    #line = fp.readline().strip()
    #print("0",(not line),"0")
    #nf.write(line)
    count = 1
    while line:
        print("Line {} : {}".format(count, line.strip()))
        #line = fp.readline()
        nf.write(line.strip())
        line = fp.readline()
        count += 1




#filepath = 'read_this.txt'
#with open(filepath) as fd:
 #   for count, line in enumerate(fd):
  #      print('File {}: {}'.format(count, line))
