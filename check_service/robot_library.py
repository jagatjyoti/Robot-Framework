#!/usr/bin/python
 
import subprocess
import os
import sys
 
def run_testcase(tcid):
        cmd = 'python tcid'
        p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
        output, err = p.communicate()
        print output
        print err