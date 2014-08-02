#!/home/action/python3/bin/python

#http://www.openlogic.com/wazi/bid/315666/Developing-a-pubsub-application-in-Redis

import redis
import sys
import time

#import ckdutil
#from ckdutil import *

class DasdServer:
      key = 'herc'      
      cmds = [1,'qq','SATK-rdRec','SATK-wrtRec']

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
          print("(findCmd)cmds :",DasdServer.cmds)
          print("(findCmd) looking for cmd '%s':" % cmd)
          try:
              self.cmdIndex = DasdServer.cmds.index(cmd)
          #if(self.cmdIndex):
              print("(findCMD OK found at %d" % self.cmdIndex)
              self.keyName = DasdServer.cmds[self.cmdIndex]
              return True
          except:
          #else:
            print("(findCMD)cmd:'%s' Not Found" % cmd)
            return False


      def parse(self,keyName):
          print("(parse) keyName:",keyName)
          keys = self.redis.hkeys(keyName)
          #print("(parse) hkeys :",self.redis.hkeys(keyName))
          print("(parse) hvals :",keys)
          print("(parse) hvals :",self.redis.hvals(keyName))
          for k in keys:
              v = self.redis.hget(keyName,k)
              print("key: %s val:%s type:%s" % (k,v,type(v)) )

      def doRead2(self):
          self.parse(self.keyName)
          # ....ckdutil stuff

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
                       print("calling doRead with self.cmdIndex :",self.cmdIndex)
                       self.doRead2()
                   else:
                       print("(getMsgs) unknown cmd : '%s'" % cmd)

                time.sleep(0.101)


t2305 = DasdServer('t2305')