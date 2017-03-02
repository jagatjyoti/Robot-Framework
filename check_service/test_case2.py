#!/usr/bin/python

from library import *

cmd = 'systemctl status sshd'
print "========================================"
print "         Checking ssh service           "
print "========================================"
exec_command(cmd)