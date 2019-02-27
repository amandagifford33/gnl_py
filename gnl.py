#filepath = read_this.txt
#new = new.txt 
#get_next_line(filepath)

#with open(filepath) as fp, open(new, 'wt') as nf:
class Gnl(object):
        def __init__(self, filepath, new, count=1):
                self.count = count
                self.filepath = filepath
                self.new = new

        def get_next_line(self):
                print('yes')
                with open(self.filepath) as fp, open(self.new, 'wt') as nf:
                        while self.count:
                                line = fp.readline().strip()
                                self.count -= 1
                        print(line)
                        nf.write(line)

#if __name__ == "__main__":
    #import sys
    #get_next_line(int(sys.argv[1]))