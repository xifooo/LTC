#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   demo_sec.py
@Time    :   2022/11/15 09:46:07
'''
import platform as pf
import socket, re, uuid, json, psutil, logging, os


def get_computer_info():
    info = {}
    
    # 系统与硬件信息
    info['platform'] = pf.system()
    info['platform-release'] = pf.release()
    info['platform-version'] = pf.version()
    info['architecture'] = pf.machine()
    info['processor'] = pf.processor()
    info['RAM'] = f"{str(round(psutil.virtual_memory().total / (1024.0 **3)))} GB"
    
    # 网络信息
    info['hostname'] = socket.gethostname()
    # info["USERNAME: 用户名"] = os.environ["USERNAME"]
    info['ip-address'] = socket.gethostbyname(socket.gethostname())
    info['mac-address'] = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    
    return json.dumps(info, 
                      indent=4, 
                      ensure_ascii=False)
    

def main():
    try:
        print(json.loads(get_computer_info()))
    except Exception as e:
        logging.exception(e)


if __name__ == "__main__":
    main()
    # print(json.loads(get_computer_info()))
