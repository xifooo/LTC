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
    
    # # 系统与硬件信息
    info['platform'] = pf.system()
    info['platform-release'] = pf.release()
    info['platform-version'] = pf.version()
    # CPU
    info['architecture'] = pf.machine()
    info['processor'] = pf.processor()
    info["CPU逻辑数量:核心数与超线程取之最高值"] = psutil.cpu_count()
    info["CPU物理核心:真正的核心数"] = psutil.cpu_count(logical=False)
    info["CPU的用户\系统\空闲时间"] = f"{psutil.cpu_times()}"
    info["CPU各核心的使用率"] = f"{psutil.cpu_percent(interval=1, percpu=True)}"
    # 内存
    info['物理内存svmem - RAM'] = f"{round(psutil.virtual_memory().total / (1024.0 **3))} GB"
    info['交换内存sswap'] = f"{round(psutil.swap_memory().total / (1024.0 **3))} GB"
    # 磁盘
    info['磁盘分区信息'] = f"{psutil.disk_partitions()}"
    info['(当前)磁盘使用情况'] = f"{psutil.disk_usage('/')}"

    # # 网络信息
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
