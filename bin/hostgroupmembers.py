# Display members of all host groups in nagios
import os
import socket
import csv,sys
import urllib
import json
import splunk4nagios as s4n
##### CHANGE PATH TO your distribution FIRST ############
#sys.path.append("/usr/lib/python2.6/site-packages/redis-2.0.0-py2.6.egg")
sys.path.append( s4n.redispath )
import redis

#FOO = "GET hostgroups\nColumns: name members_with_state\nSeparators: 10 10 44 124"
FOO = "GET hostgroups\nColumns: name members_with_state\nOutputFormat: python\n"

def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.send(content)
    s.shutdown(socket.SHUT_WR)
    data = s.recv(100000000)
    print "Connection closed."
    s.close()
    return data

data = netcat( s4n.server, s4n.mk_port, FOO ) 
print data

# output should look like this:
# host_name,state,num,hostgroup
# arn-grnhse-sw1,0,1,00010
# arn-hunnewell-3-sw1,0,1,00010
