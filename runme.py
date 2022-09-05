import argparse
from Report import Report
# 要上传的数据
report_data =[
    ("jinji_lxr", "lxr"),
    ("jiji_mobile", "12345"),
    ("jinji_guanxi", "父"),
    ("juzhudi", "东校区"),
    ("dorm_building","365"),
    ("dorm","304"),
    ("body_condition", "1"),
    ("body_condition_detail", ""),
    ("has_fever", "0"),
    ("last_touch_sars", "0"),
    ("last_touch_sars_date", ""),
    ("last_touch_sars_detail", ""),
    ("is_danger", "0"),
    ("is_goto_danger", "0"),
    ("other_detail", "")
]
cross_campus_data = [
    ("return_college[]", "东校区"),  # 往返校区
    ("return_college[]", "西校区"),  # 往返校区
    #("return_college[]", "南校区"),  # 往返校区
    #("return_college[]", "北校区"),  # 往返校区
    ("return_college[]", "中校区"),  # 往返校区
    ("reason", "去图书馆"),  # 原因
]
out_school_data = [
    ("return_college[]", "蜀山区"),  # 目的地
    ("return_college[]", "包河区"),  # 目的地
    ("return_college[]", "瑶海区"),  # 目的地
    ("return_college[]", "庐阳区"),  # 目的地
    ("reason", "去商场"),  # 原因
]
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="学号密码必填. 其余项选填, 语法是 -a (表示y), -a y 或 -a n, 空缺则采取默认值")
    parser.add_argument("stuid", help="学号", type=str)
    parser.add_argument("password", help="密码", type=str)
    parser.add_argument("jjlxr", help="紧急联系人", type=str)
    parser.add_argument("jjdh", help="紧急电话", type=str)
    parser.add_argument('-r', help="上报健康信息, 默认值y",nargs='?', default='y',const='y',choices=['y','n'],metavar='y/n')
    parser.add_argument('-u',help="更新行程卡, 默认值y", nargs='?', default='y',const='y',choices=['y','n'],metavar='y/n')
    parser.add_argument('-c', help="跨校区, 默认值n", nargs='?', default='n',const='y',choices=['y','n'],metavar='y/n')
    parser.add_argument('-o',help="出校, 默认值n",nargs='?',  default='n',const='y',choices=['y','n'],metavar='y/n')
    args = parser.parse_args()
    autorepoter = Report(stuid=args.stuid, password=args.password)
    report_data[0]=("jinji_lxr", args.jjlxr)
    report_data[1]=("jiji_mobile", args.jjdh)
    autorepoter.login.login()
    if args.r=='y':
        autorepoter.report(report_data)
    if args.u=='y':
        autorepoter.upload_code()

    state=autorepoter.getstate()
    if args.c=='y':
        if state != '在校':
            print(state+", 不做跨校报备")
            exit(-1)
        else:
            autorepoter.cross_campus(cross_campus_data)
    if args.o=='y':
        if state != '在校':
            print(state+", 不做出校报备")
            exit(-1)
        else:
            autorepoter.out_school(out_school_data)
