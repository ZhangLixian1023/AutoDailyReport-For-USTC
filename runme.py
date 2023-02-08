import argparse
from Report import Report
# 要上传的数据
report_data =[
    ("juzhudi","河南省郑州市新郑市"),
    ("q_0","良好"),
    ("body_condition_detail",""),
    ("q_2",""),
    ("q_3",""),
    ("jinji_lxr", "zxx"),
    ("jinji_guanxi", "父"),
    ("jiji_mobile", "4214"),
    ("other_detail", "")
]
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("stuid", help="学号", type=str)
    parser.add_argument("password", help="密码", type=str)
    parser.add_argument("jjlxr", help="紧急联系人", type=str)
    parser.add_argument("jjdh", help="紧急电话", type=str)
    args = parser.parse_args()
    autorepoter = Report(stuid=args.stuid, password=args.password)
    report_data[5]=("jinji_lxr", args.jjlxr)
    report_data[7]=("jiji_mobile", args.jjdh)
    autorepoter.login.login()
    autorepoter.report(report_data)
