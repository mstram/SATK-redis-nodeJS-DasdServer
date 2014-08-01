#!/home/action/python3/bin/python 

import redis
import sys

r = redis.Redis("localhost")
#r = redis.Redis("zop")

#r.publish(sys.argv[1],"["+sys.argv[2]+"] " + " ".join(sys.argv[3:]))

#r.publish(sys.argv[1],sys.argv[2]) 

#data = "stuff"
#data = [0,1,3,'key01','the data for cyl=0, hd=1,r=3']

chan ='herc'
cmd  ='rdrec'
print("sending to channel '%s'  cmd: '%s' " % (chan,cmd))

#r.hmset(['cmd:','id:','0001','op:','rd','no:','001','cyl:','0','hd:','1','r:','2'])

#r.miketest('foo')

def foo(p1,p2):
  print("foo p1: p2",p1,p2)
  
try:
    r.hmset('cmd03:',{'id': '0001', 'op': 'rd','no': '001', 'cyl': '0', 'hd': '1', 'r': '2'})
    print("(hsend) setting redis:'cmd03'")
    #r.hmset('cmd03:',"'id:','0001','op:','rd'")
    #r.hmset('cmd03',{'id': 1, 'op': 'rd'})
    #foo('cmd03',{'id': 1, 'op': 'rd'} )
except:
  print("some error with hmset: ",sys.exc_info()[1])
  print(sys.exc_info())

r.publish(chan,cmd)   # Send 'rd' cmd to 'herc' channel  that key 'cmd1' has been updated
                      # The dasd server will receive the message and invoke the ckdutil routines  
  
def t1():
  print("(hsend)(not reached ???)")
  r.hset('cmd1:','id:','0001')
  r.hset('cmd1:','op:','rd')
  r.hset('cmd1:','no:','001')
  r.hset('cmd1:','cyl:','0')
  r.hset('cmd1:','hd:','1')
  r.hset('cmd1:','r:','2')


