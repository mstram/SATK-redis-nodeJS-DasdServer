#!/home/action/python3/bin/python

#http://www.openlogic.com/wazi/bid/315666/Developing-a-pubsub-application-in-Redis

import redis
import sys
import time

import ckdutil
from ckdutil import *

class DasdServer:
      key = 'herc'      
      cmds = ['SATK-rdRec','SATK-wrtRec']
      
      
      def __init__(self,name):
          
          print("(DasdServer v 0.001)(init) name:",name)
          self.name = name
          #self.redis = redis.Redis("localhost")
          self.redis = redis.Redis("pub-redis-10388.us-east-1-4.1.ec2.garantiadata.com",10388)
          #print("Waiting for redis: %s '" % sys.argv[1] +"'")
          self.p = self.redis.pubsub()
          #self.p.subscribe(sys.argv[1])
          #self.key = "herc"
          self.p.subscribe("herc")

          self.getMsgs();

          
      def findCmd(self,cmd):
          print("\n")
          print("(findCmd) looking for cmd '%s':" % cmd)
          try:
            return DasdServer.cmds.index(cmd)
          except:
            return False
    
          
      def parse(self,keyName):
          print("(parse) keyName:",keyName)
          print(self.redis.hvals(keyName))
          
      def doRead(self,keyName):
          print("---- doRead ---")
          print("self.redis.hvals keyName '%s'' :",keyName)
          self.parse(keyName)
          
      def pt(self,n,ob):
          print("type(" +n +")")
          print(type(ob))

      def getMsgs(self):
          smsg = "SATK-Dasd Server : Waiting for msg: %s '" % DasdServer.key +"'"
          #print("(SATK-Dasd Server : Waiting for msg: %s '" % key +"'")
          print(smsg)
          while True:
                message = self.p.get_message()
                if message:
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
                       #raise "unknown cmd :",cmd

                   r = self.findCmd(cmd)
                   #if(cmd == "rdrec"):
                   if(r): 
                       print("calling rd")
                       self.doRead(cmd)
                   else:
                       print("(getMsgs) unknown cmd : '%s'" % cmd)

                time.sleep(0.101)


t2305 = DasdServer('t2305')