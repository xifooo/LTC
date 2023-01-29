#!/usr/bin/env python
# -*- encoding: utf-8 -*-
''' 
@File    :   datetime_module.py
@Time    :   2022/11/11 16:43:28
'''
from datetime import date, time, datetime, timezone, tzinfo, timedelta


def preface():
    info = {}
    info["date"] = "指日期, datetime.date(2022, 01, 01) = 2022-01-01"
    info["time"] = "指时间, datetime.time(13, 40, 59, 11) = 13:40:59 11"
    info["datetime"] = "日期+时间, datetime.datetime(2022, 11, 12, 12, 56, 48, 467797)"
    
    info["timedelta"] = "表示两个date、time、datetime实例之间的时间差"
    info["tzinfo"] = "时区TimeZone相关信息对象的抽象基类。"
    info["timezone"] = "UTC的固定偏移量"
    return info

def dt_date():
    info = {}
    # 查
    info["date.max: date对象能表示的最大日期"] = f"{date.max}"
    info["date.min: date对象能表示的最小日期"] = f"{date.min}"
    info["date.resolution: date对象日期的最小单位"] = f"{date.resolution}"
    d = date.today()
    info["d = date.today(): 当前本地日期的date对象"] = f"{d}"
    info["d.year: 年"] = f"{d.year}"
    info["d.month: 月"] = f"{d.month}"
    info["d.day: 日"] = f"{d.day}"
    info["d.weekday(): 星期, [0,6]"] = f"{d.weekday()}"
    info["d.isoweekday(): 星期, [1,7]"] = f"{d.isoweekday()}"
    # 改
    info["d.replace(year,month,day): 生成并返回一个新的date对象, 原date对象不变"] = f"{d.replace(2000, 1, 1)}"
    # 格式与类型的转换
    info["d.toordinal(): 日期d是自 0001-01-01 开始的第多少天"] = f"{d.toordinal()}"
    info["d.isoformat(): date对象 -> 'YYYY-MM-DD'格式的字符串"] = f"{d.isoformat()}"
    info["d.strftime(): date对象 -> 指定格式的字符串, 等同于time.strftime(format, struct_time)"] = f"{d.strftime('%d;%m;%Y')}"
    info["date.fromtimestamp(timestamp): 时间戳 -> date对象"] = f"{d.fromtimestamp(738471)}"
    info["d.timetuple(): date对象 -> time.struct_time对象"] = f"{d.timetuple()}"
    info["d.isocalendar(): date对象 -> IsoCalendarDate对象(iso的周六为6)"] = f"{d.isocalendar()}"
    return info
    
    
def dt_time():
    info = {}
    # 增
    t = time(23, 59, 59, 999999)
    # 查
    info["time.max: time对象能表示的最大时间"] = f"{time.max}"
    info["time.min: time对象能表示的最小时间"] = f"{time.min}"
    info["time.resolution: time对象的最小单位, 即两个不同时间的最小差值为1微秒"] = f"{time.resolution}"
    info["t.hour: 时"] = f"{t.hour}"
    info["t.minute: 分"] = f"{t.minute}"
    info["t.second: 秒"] = f"{t.second}"
    info["t.microsecond: 微秒"] = f"{t.microsecond}"
    info["t.tzinfo: 返回传递给time构造方法的tzinfo对象, 如果该参数未给出, 则返回None"] = f"{t.tzinfo}"
    # 改
    info["t.replace: 生成并返回一个新的time对象, 原time对象不变"] = f"{t.replace(10,12,0)}"
    # 格式与类型的转换
    info[r"t.isoformat(): time对象 -> 'HH:MM:SS.%f'格式的字符串"] = f"{t.isoformat()}"
    info["t.strftime(): time对象 -> 指定格式的字符串, 等同于time.strftime(format, struct_time)"] = f"{t.strftime('%H%M%S.%f')}"
    return info
    
    
def dt_datetime():
    info = {}
    info["datetime.datetime = date + time"] = "年月日小时分钟秒微秒, 时区tzinfo"
    today = datetime.today()
    # 查
    info["today = datetime.today(): 当前本时区日期时间的datetime对象"] = f"{today}"
    info["datetime.datetime.now([tz]): 指定时区日期时间的datetime对象, 如果不指定tz参数则结果同datetime.today()"] = f"{today}"
    info["datetime.datetime.utcnow(): 当前utc日期时间的datetime对象"] = f"{datetime.utcnow()}"
    info["today.date(): 获取datetime对象对应的date对象"] = f"{today.date()}"
    info["today.time(): 获取datetime对象对应的time对象,  tzinfo为None"] = f"{today.time()}"
    info["today.timetz(): 获取datetime对象对应的time对象, tzinfo与datetime对象的tzinfo相同"] = f"{today.timetz()}"
    info["today.weekday(): 获取datetime对象对应的date对象"] = f"{today.date()}"
    info["today.toordinal(): 日期时间d是自 0001-01-01 开始的第多少天"] = f"{today.toordinal()}"
    # 合并
    
    info["datetime.datetime.combine(date, time): date对象 + time对象 -> datetime对象"] = "datetime.combine(date.today(),time(23,59,59,999999))"
    # 改
    info["datetime.replace():生成并返回一个新的datetime对象, 如果所有参数都没有指定, 则返回一个与原datetime对象相同的对象"] = f"{today.replace()}"
    
    # 格式与类型的转换
    info["datetime.datetime.fromtimestamp(timestamp[, tz]): 时间戳 -> datetime对象"] = f"{datetime.fromtimestamp(738471)}"
    info["datetime.datetime.utcfromtimestamp(timestamp[, tz]): 时间戳 -> utcdatetime对象"] = f"{datetime.utcfromtimestamp(738471)}"
    info["datetime.datetime.timestamp(): datetime对象 -> 时间戳"] = f"{datetime.timestamp(datetime.now())}"
    
    info["today.timetuple(): datetime对象 -> time.struct_time对象, 不含tzinfo"] = f"{today.timetuple()}"
    info["today.utctimetuple(): datetime对象 -> utc时间的time.struct_time对象, 不含tzinfo"] = f"{today.utctimetuple()}"
    
    info["datetime.datetime.strptime(date_str, format): 字符串 -> datetime对象"] = f"{datetime.strptime('2017/05/04 10:23', '%Y/%m/%d %H:%M')}"
    info["today.isoformat(): datetime对象 -> 字符串"] = f"{today.isoformat()}"
    info["today.strftime(format): datetime对象 -> 指定格式的字符串"] = f"{today.strftime('%Y--%m--%d')}"
    info["today.isocalendar(): datetime对象 -> IsoCalendarDate对象(iso的周六为6)"] = f"{today.isocalendar()}"
    info["today.ctime(): 等价于time模块的time.ctime(time.mktime(d.timetuple()))"] = f"{today.ctime()}"
    return info
    
def dt_timedelta():
    info = {}
    info["timedelta(365).total_seconds(): 一年包含的总秒数"] = f"{timedelta(365).total_seconds()}"
    td = datetime.now() - datetime.utcnow()
    info["td = datetime.datetime.now() - datetime.datetime.utcnow()"] = f"{td}"
    info["td.days, td.seconds, td.microseconds: 天 [-999999999, 999999999], 秒[0, 86399], 微秒[0, 999999]"] = f"{td.days, td.seconds, td.microseconds}"
    info["创建一个timedelta: "] = """delta = timedelta(
                                    days=50,
                                    seconds=27,
                                    microseconds=10,
                                    milliseconds=29000,
                                    minutes=5,
                                    hours=8,
                                    weeks=2
                                )"""
    now = datetime.now()
    info["现在是now: "] = f"{now}"
    info["三天后(now + timedelta): "] = f"{now + timedelta(3)}" # 第一个位置参数为days
    
    info["三小时后(now + timedelta): "] = f"{now + timedelta(hours=3)}"
    info["三小时前(now + timedelta): "] = f"{now + timedelta(hours=-3)}"
    info["一天三小时零三分钟后(now + timedelta): "] = f"{now + timedelta(days=1, hours=3, minutes=3)}"
    return info
    
    
def dt_timezone():
    info = {}
    return info
    
    
def dt_tzinfo():
    info = {}
    return info
    

def main():
    return {**dt_date(), **dt_time(), **dt_datetime(), **dt_timedelta(), **dt_timezone(), **dt_tzinfo()}
    

if __name__ == "__main__":
    info = main()
    import pathlib, json
    curdir = pathlib.Path(__file__)
    name = curdir.stem
    with open(f"{curdir.parent}/{name}.json", "w") as f:
        f.write(json.dumps(info, 
                           indent=4, 
                           ensure_ascii=False,
                           # encoding = "utf-8",  # py3.9已经移除了
                           skipkeys=False
                           ))
