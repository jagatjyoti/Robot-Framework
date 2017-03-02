#!/usr/bin/python

from library import *

cmd = 'systemctl status docker'
print "========================================"
print "       Checking docker service          "
print "========================================"
exec_command(cmd)