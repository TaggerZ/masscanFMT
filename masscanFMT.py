# -*- coding: UTF-8 -*-
from xml.dom.minidom import parse
import xml.dom.minidom
import sys
import os

if(len(sys.argv) == 2):
    filename = sys.argv[1]
    if(os.path.exists(filename)):
        DOMTree = xml.dom.minidom.parse(filename)
        collection = DOMTree.documentElement
        hosts = collection.getElementsByTagName("host")
        outName = "%s.txt"%(filename)
        with open(outName, 'w') as f:
            for host in hosts:
                address = host.getElementsByTagName('address')[0]
                ip = address.getAttribute("addr")
                ports = host.getElementsByTagName('ports')[0]
                port = ports.getElementsByTagName('port')[0]
                portid = port.getAttribute("portid")
                res = "%s:%s" % (ip, portid)
                f.write(res + '\n')
                print res
    else:
        print "文件不存在"
else:
    print "*   masscanFMT.py a.xml"
    print "*   create a file suffix `.txt` in source file path"
