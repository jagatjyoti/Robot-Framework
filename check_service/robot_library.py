#!/usr/bin/python
 
import subprocess
import os
import sys

global tcid 
tcid = ''

#def tc_path(tcid):
#	tc_path = os.getcwd() + tcid
#        return tc_path
 
def run_testcase(tcid):
        cmd = 'python ' + tcid  
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = p.communicate()
        print output
        print err
        if err != 0 and output == 0:
            return False
        else:
            return True


def get_result(tcid):
	status = run_testcase(tcid)
	if status == False: 
	    print "Failed to execute " + tcid + ". Exiting ..."
            sys.exit(1)
