#!/home/action/python3/bin/python

#http://www.openlogic.com/wazi/bid/315666/Developing-a-pubsub-application-in-Redis

import redis
import sys
import time

import ckdutil
from ckdutil import *

class DasdServer:
      key = 'herc'      
      def __init__(self,name):
          
          print("(DasdServer v 0.001)(init) name:",name)
          self.name = name
          self.redis = redis.Redis("localhost")
          #print("Waiting for redis: %s '" % sys.argv[1] +"'")
          self.p = self.redis.pubsub()
          #self.p.subscribe(sys.argv[1])
          #self.key = "herc"
          self.p.subscribe("herc")

          self.getMsgs();

       
      def doRead(self):
          print("---- doRead ---")
          print("self.redis.hvals cmd03:")
          print(self.redis.hvals('cmd03:'))

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

                   if(cmd == "rdrec"):
                       print("calling rd")
                       self.doRead()
                   else:
                       print("(getMsgs) unknown cmd : '%s'" % cmd)

                time.sleep(0.101)


t2305 = DasdServer('t2305')