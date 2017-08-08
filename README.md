# Introduction

Robot Framework stitched with Python can be a great stack for testing.

## Prerequisites

You must have [Python](https://www.python.org/downloads/) and [Robot Framework](http://robotframework.org/) installed on your machine. 

## What's in here

A beginner level Robot Framework code which ideally does a service check (for docker and sshd) on a remote machine. Most of which is python code with minimal robo code.

## Execution

Run the robot file which carries all your testcases. 

```
$ robot service.robot
```

## Output

```
$ robot service.robot
==============================================================================
Service :: Test Suite for functionality of Service check
==============================================================================
Execute test_case1 :: Checking if docker service is running fine      | PASS |
------------------------------------------------------------------------------
Execute test_case2 :: Checking if ssh deamon is running fine          | PASS |
------------------------------------------------------------------------------
Service :: Test Suite for functionality of Service check              | PASS |
2 critical tests, 2 passed, 0 failed
2 tests total, 2 passed, 0 failed
==============================================================================
Output:  /home/zarvis/Robot-Framework/check_service/output.xml
Log:     /home/zarvis/Robot-Framework/check_service/log.html
Report:  /home/zarvis/Robot-Framework/check_service/report.html
```

P.S: Move all the above files to default directory of your webserver (/var/www/html in my case) and check logs in browser. :) 
