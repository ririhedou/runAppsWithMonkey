#!/usr/bin/env python

"""
ketian @ 2016
The code to automatically run the apps

"""

import os,re,sys,subprocess
import time


def get_package_list():
    subprocess.call("adb root | adb pull /data/system/packages.list packages.list", shell=True)


def runOnDevice():
    subprocess.call("adb devices", shell=True)
    pass


def run_package_with_monkey(packagename):
    cmd = "adb shell monkey " + " -p " + packagename +" -v 100"
    cmd2 = "adb logcat"

    #print (cmd)
    p1 = subprocess.Popen(cmd, shell=True)
    p2 = subprocess.Popen(cmd2, stdout=subprocess.PIPE, shell=True)

    p1.wait()
    p2.kill()

def run_packagelist_with_monkey(packagenamelist):
    cmd = "adb shell monkey "

    for i in packagenamelist:
        cmd +=  " -p " + i
    cmd +=  " -v 1000"

    print (cmd)
    cmd2 = "adb logcat"

    p1 = subprocess.Popen(cmd, shell=True)
    p2 = subprocess.Popen(cmd2, stdout=subprocess.PIPE, shell=True)

    p1.wait()
    p2.kill()



if __name__ == "__main__":
    s = "inst"
    run_packagelist_with_monkey(s)
