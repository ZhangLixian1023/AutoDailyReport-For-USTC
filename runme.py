import argparse
import datetime
import pytz
from Report import Report
# 要上传的数据
report_data =[
    ("juzhudi","东校区"),
    ("dorm_building","365"),
    ("dorm","304"),
    ("q_0","良好"),
    ("body_condition_detail",""),
    ("q_2",""),
    ("q_3",""),
    ("jinji_lxr", "zxx"),
    ("jinji_guanxi", "父"),
    ("jiji_mobile", "4214"),
    ("other_detail", "")
]
cross_campus_data=[
    ("start_date", "2023-02-20 23:49:32"),
    ("end_date","2023-02-21 23:59:59"),
    ("return_college[]","东校区"),
    ("return_college[]","西校区"),
    ("return_college[]","中校区"),
    ("reason","校内上课/考试"),
    ("comment",""), 
    ("t","3")
]
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("stuid", help="学号", type=str)
    parser.add_argument("password", help="密码", type=str)
    parser.add_argument("jjlxr", help="紧急联系人", type=str)
    parser.add_argument("jjdh", help="紧急电话", type=str)
    args = parser.parse_args()
    autorepoter = Report(stuid=args.stuid, password=args.password)
    report_data[7]=("jinji_lxr", args.jjlxr)
    report_data[9]=("jiji_mobile", args.jjdh)
    t=datetime.datetime
    tz=pytz.timezone('Asia/Shanghai')
    t_now=t.now(tz)
    t_start=t_now.replace(minute=t_now.minute-1)
    t_end=t_start.replace(hour=23,minute=59,second=59)
    cross_campus_data[0]=("start_date",t_start.strftime("%Y-%m-%d %H:%M:%S"))
    cross_campus_data[1]=("end_date",t_end.strftime("%Y-%m-%d %H:%M:%S"))
    autorepoter.login.login()
    autorepoter.report(report_data)
    autorepoter.cross_campus(cross_campus_data)