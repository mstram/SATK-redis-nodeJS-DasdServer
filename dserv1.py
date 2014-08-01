#!/home/action/python3/bin/python 

#http://www.openlogic.com/wazi/bid/315666/Developing-a-pubsub-application-in-Redis

import redis
import sys
import time

import ckdutil
from ckdutil import *

r = redis.Redis("localhost")
p = r.pubsub()
#p.subscribe(sys.argv[1])
key = "herc"
p.subscribe("herc")


def doRead():
  print("---- doRead ---")
  print("r.hvals cmd03:")
  print(r.hvals('cmd03:'))

def pt(n,ob):
  print("type(" +n +")")
  print(type(ob))

#print("Waiting for redis: %s '" % sys.argv[1] +"'")

smsg = "SATK-Dasd Server : Waiting for msg: %s '" % key +"'"
#print("(SATK-Dasd Server : Waiting for msg: %s '" % key +"'")
print(smsg)
while True:
  message = p.get_message()
  if message:
    # do something with the message
    print("---------- new msg ---------------------")
    print(message)
    
    #print("message['data']")
    #print(message['data'])
    print(smsg)
    #print("len(message) :%d" % len(message))
    #print("len(message['data']) :%d" % len(message['data']))
    
    bdata = message['data']
    print("bdata:")
    print(bdata)
    try:
      cmd = bdata.decode("utf-8")
    except:
      cmd = bdata

    if(cmd == "rdrec"):
      print("calling rd")
      doRead()
    else:
      print("unknown cmd : '%s' " % cmd)
    
    #print("len(data]) :%d" % len(data))
    # pt('bdata',bdata)
    # pt('data',data)
    
    #for item in message:
      #print(item['data'])
  #time.sleep(0.001)  # be nice to the system :)
  time.sleep(0.101) 


#for item in ps_obj.listen():
#    print(item['data'])