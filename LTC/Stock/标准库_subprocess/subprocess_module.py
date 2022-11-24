#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   subprocess_module.py
@Time    :   2022/11/09 22:18:55
'''
import subprocess, os


def win_sys_cmd():
    run_cmd = subprocess.run(
        args= "echo hello world!",
        stdout= subprocess.PIPE,
        stderr= subprocess.STDOUT,
        shell= True,
        encoding=None
        )
    # 中文win系统以gbk编码
    print(run_cmd.stdout.decode("gbk"))
    
    popen_cmd = subprocess.Popen(
        args= "echo hello world!",
        stdout= subprocess.PIPE,
        stderr= subprocess.STDOUT,
        shell= True,
        encoding="utf8"
        )
    for line in popen_cmd.stdout.readlines():
        print(line)
    print(popen_cmd.stdout.readline())
    
    

def linux_sys_cmd():
    os.system("ps aux |grep python |awk '{print $2}' |xargs kill")
    
    proc1 = subprocess.Popen(['ps', 'aux'], 
                             stdout=subprocess.PIPE)
    proc2 = subprocess.Popen(['grep', 'python'], 
                             stdin=proc1.stdout, 
                             stdout=subprocess.PIPE, 
                             stderr=subprocess.PIPE)
    proc3 = subprocess.Popen(['awk', "'{print $2}'"], 
                             stdin=proc2.stdout, 
                             stdout=subprocess.PIPE, 
                             stderr=subprocess.PIPE)
    proc4 = subprocess.Popen(['xargs', 'kill'], 
                             stdin=proc3.stdout, 
                             stdout=subprocess.PIPE, 
                             stderr=subprocess.PIPE)
    proc1.stdout.close() # Allow proc1 to receive a SIGPIPE if proc2 exits.
    proc2.stdout.close() # Allow proc2 to receive a SIGPIPE if proc3 exits.
    proc3.stdout.close() # Allow proc3 to receive a SIGPIPE if proc4 exits.
    out, err = proc4.communicate()

    
    
if __name__ == "__main__":
    win_sys_cmd()
