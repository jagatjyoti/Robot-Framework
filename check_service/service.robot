*** Settings ***
 
Documentation           Test Suite for functionality of Service check
Force Tags              This is test. This is test.
Library                 robot_library.py
 
 
*** Variables ***
 
${TestSuite}            robot_framework
 
 
*** Test Cases ***
 
Execute test_case1
        [Documentation]    Checking if docker service is running fine
        [Tags]    This is for tagging
        run_testcase    test_case1.py
 
 
Execute test_case2
        [Documentation]    Checking if ssh deamon is running fine
        [Tags]    This is for tagging
        run_testcase    test_case2.py
 