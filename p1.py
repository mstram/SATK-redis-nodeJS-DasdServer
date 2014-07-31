#!/home/action/python3/bin/python 
# !/usr/bin/python
#
import sys
def t1(p1,p2,p3):
    #print("(p1.py) p1: %s  p2:%s  p3:$s" % (p1,p2,p3) )
    print('p1,p2,p3')
    print(p1)
    print(type(p1))
    print
    print(p2)
    print(type(p2))
    print
    print(p3)
    print(type(p3))
    return [42,'abc']
  
p1 = str(sys.argv[1])
p2 = str(sys.argv[2])
p3 = str(sys.argv[3])  
print("python version %s" % sys.version)  
t1(p1,p2,p3)
