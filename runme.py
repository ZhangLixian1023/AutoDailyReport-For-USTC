import argparse
from Report import Report

report_data = [
    "juzhudi": "河南省郑州市新郑市",
    "body_condition": "1",
    "body_condition_detail": "",
    "has_fever": "0",
    "last_touch_sars": "0",
    "last_touch_sars_date": "",
    "last_touch_sars_detail": "",
    "is_danger": "0",
    "is_goto_danger": "0",
    "jinji_lxr": "张昆",
    "jinji_guanxi": "父",
    "jiji_mobile": "13803714909",
    "other_detail": ""
]
cross_campus_data = [
    ("return_college[]", "东校区"),  # 往返校区
    ("return_college[]", "西校区"),  # 往返校区
    ("return_college[]", "南校区"),  # 往返校区
    ("return_college[]", "北校区"),  # 往返校区
    ("return_college[]", "中校区"),  # 往返校区
    ("reason", "上课"),  # 原因
]
out_school_data = [
    ("return_college[]", "蜀山区"),  # 目的地
    ("return_college[]", "包河区"),  # 目的地
    ("return_college[]", "瑶海区"),  # 目的地
    ("return_college[]", "庐阳区"),  # 目的地
    ("reason", "玩"),  # 原因
]
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="URC nCov auto report script.")
    parser.add_argument("stuid", help="your student number", type=str)
    parser.add_argument("password", help="your CAS password", type=str)
    args = parser.parse_args()
    autorepoter = Report(stuid=args.stuid, password=args.password)
    count = 5
    while count != 0:
        if autorepoter.getstate() != '在校':
            print("WRONG STATE")
            exit(0)
        if (autorepoter.report(report_data)
                & autorepoter.upload_code()
                & autorepoter.cross_campus(cross_campus_data)
                & autorepoter.out_school(out_school_data)):
            print("ENJOY YOUR FREEDOM! ")
            break
        print("Retry...")
        count = count - 1
    if count != 0:
        exit(0)
    else:
        exit(-1)
