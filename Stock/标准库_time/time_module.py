#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   time_module.py
@Time    :   2022/11/11 15:46:31
'''
import time

def preface():
    info = {}
    info["time模块目前只支持到2038年前"] = "请使用datetime模块"
    info["UTC(Coordinated Universal Time, 世界协调时), 亦即格林威治天文时间, 世界标准时间"] = "中国为东八区, 比UTC早8个小时, 也就是UTC+8"
    info["DST"] = "DST(Daylight Saving Time)即夏令时"
    info["时间戳(timestamp): time.time()"] = "1970年1月1日之后的秒"
    info["格式化的时间字符串(string_time): time.localtime()"] = "年-月-日 时:分:秒, 如2017-09-26 09:12:48"
    info[r"结构化时间(struct_time): time.strftime('%Y-%m-%d')"] = r"年-月-日 时:分:秒的多元元组, 例如time.struct_time(tm_year=2017, tm_mon=9, tm_mday=26, tm_hour=9, tm_min=14, tm_sec=50, tm_wday=1, tm_yday=269, tm_isdst=0), 可以通过time.strftime('%Y-%m-%d')获得。"
    return info

def chief_methods():
    info = {}
    
    info["time.sleep(t): 睡眠或者暂停程序t秒"] = "time.sleep(900)"
    # 查
    info["time.time(): 当前系统时间戳"] = "time.time()"
    
    # # 转换
    # info["time.gmtime([secs]): 将一个时间戳转换为UTC时区的结构化时间"] = f"{time.gmtime(time.time() - 10000)}"
    # info["time.localtime([secs]): 将一个时间戳转换为当前时区的结构化时间"] = f"{time.gmtime(time.time() - 10000)}"
    # info["time.ctime([secs]): 将一个时间戳转换为本地时间的格式化字符串, 默认使用time.time()作为参数"] = f"{time.ctime()}"
    # info["time.asctime([t]): 一个结构化时间转换为Sun Aug 23 14:31:59 2017这种形式的格式化时间字符串。默认将time.localtime()作为参数。"] = f"{time.asctime()}"
    # # 逆转换
    # info["time.mktime(t): 将一个结构化时间转化为时间戳。 time.mktime()执行与gmtime(),localtime()相反的操作"] = f"{time.mktime(1406391907)}"
    # # 格式化
    # info[r"time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime()): 格式化字符串表示的当地时间"] = f"{time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime())}"
    # info[r"time.strptime('2017-09-26 12:11:30','%Y-%m-%d %H:%M:%S'): 格式化时间字符串转化成结构化时间"] = f"{time.strptime('2017-09-26 12:11:30','%Y-%m-%d %H:%M:%S')}"
    
    # 时间戳 <-> 结构化时间
    info["时间戳 -> UTC结构化时间"] = "time.gmtime()"
    info["时间戳 -> 本地结构化时间"] = "time.localtime()"
    info["UTC结构化时间 -> 时间戳"] = "calendar.timegm()"
    info["本地结构化时间 -> 时间戳"] = "time.mktime()"
    
    # 结构化时间 -> 格式化字符串
    info["结构化时间 -> 格式化字符串"] = "time.strftime()"
    info["格式化字符串 -> 结构化时间"] = "time.strptime()"
    return info
    

def main():
    info = {}
    info = {**preface(), **chief_methods()}
    return info


if __name__ == "__main__":
    info = main()
    
    import pathlib, json
    
    curdir = pathlib.Path(__file__)
    name = curdir.stem
    with open(f"{curdir.parent}/{name}.json", "w") as f:
        f.write(json.dumps(info, 
                           indent=4,
                           ensure_ascii=False))
