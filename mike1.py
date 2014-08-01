#!/usr/bin/python 

import ckdutil
from ckdutil import *

def hexStr(nm,ar):
    print("---- (hexStr)---" + nm)
    s = ""
    for c in ar:
        #print(c)
        s+= str(c)
    print("s: " + s)
    return s


#def write30(ck):
def writeMultRecs(ck,nrecs,cyl,hd):
    #ck = ckd.attach(fname,False)
    print("(write30)")
    print(ck.fo.name)
    ck.seek(cyl,hd,True)

    for r in range(nrecs):
        ks = hexStr("ks",[r+1])
        data = "data: " + hexStr("data",[r+1])
        print(r+1)
        ck.write(0,1,r+1,ks,data,True)

    #ck.detach(True)

def test1(fname,device):
    print("------ test1 - (create dasd, write, read)")
    print("New")
    ck = ckd.new(fname,device,None,False,True)

    ck = ckd.attach(fname,False)
    #writeMultRecs(ck,nrecs,cyl,hd):
    #writeMultRecs(ck,5,0,1)
    #ck.detach()
    #return

    #write30(ck)
    #return

    #return
    #print("ck")
    #print(ck)
    #print(ck.dev)
    #ck = ckd.attach(fname,False)   # False for RO

    print("Seek")
    r =ck.seek(0,1)
    #return
    print("write")

    ks    = hexStr("ks",[0xF0,0xF1,0xF1])
    data  = hexStr("data",[0xC1,0xC2,0xC3])

    #ck.write(cyl,hd,rec,ks,data,True)
    ck.write(0,1,1,ks,data,False)

    ks    = hexStr("ks",[0xF0,0xF1,0xF2])
    data  = hexStr("data",[0xC4,0xC5,0xC6])
    ck.write(0,1,2,ks,data,False)

    #ck.write(0,0,1,ks,data)
    #ck.write(0,1,1,ks,data)

    #print("------- detach ---------")
    #ck.detach(True)  # debug

    #seek(self,cc,hh,debug=False,dump=False):
    #print("Seek")
    #ck.seek(0,0,True)

    print("read")
    rec = ck.read(1)
    print("rec:")
    print(rec)

    print("------- detach ---------")
    ck.detach()  # debug


def read(ck,rn):
    rec = ck.read(rn)
    print("rec#: %d" % rn)
    print(rec)

def test2(fname):
    print("\n\n\n--------- test2 : read from existing DASD")
    print("-- Attach --")
    ck = ckd.attach(fname,False)

    print("-- Seek ---")
    ck.seek(0,1)

    print("read")
    read(ck,1)
    read(ck,2)
    read(ck,3)
    read(ck,4)
    read(ck,5)
   # read(ck,6)
    #read(ck,3)

    print("------- detach ---------")
    ck.detach()  # debug




test1('t2305','2305')
test2('t2305')

#test1('t3350','3350')
#test2('t3350')

#test1('h3350','3350')
#test2('h3350')

#s360-insn.msl

#write30('t3350')
#test2('t3350')