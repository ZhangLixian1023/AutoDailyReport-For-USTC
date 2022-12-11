from bs4 import BeautifulSoup
from ustclogin import Login
from datetime import timedelta
from datetime import timezone

SHA_TZ = timezone(  # 北京时间
    timedelta(hours=8),
    name="Asia/Shanghai",
)


class Report(object):

    def __init__(self, stuid, password):
        self.stuid = stuid
        self.password = password
        self.login = Login(self.stuid, self.password,"https://weixine.ustc.edu.cn/2020/caslogin")
    def getstate(self):
        data = self.login.result.text
        soup = BeautifulSoup(data, "html.parser")
        return soup.find("p", {"style":"margin: 5px -10px 0;"}).contents[1].contents[0]

    def report(self, report_data):
        data = self.login.result.text
        data = data.encode("ascii", "ignore").decode("utf-8", "ignore")
        soup = BeautifulSoup(data, "html.parser")
        token = soup.find("input", {"name": "_token"})["value"]
        data = [("_token", token)] + report_data
        url = "https://weixine.ustc.edu.cn/2020/daliy_report"
        r = self.login.session.post(url, data=data)
        alert=BeautifulSoup(r.text, 'html.parser').find(class_='alert')
        info=alert.get_text()[0:-2]
        print("健康打卡结果："+info)
        if "上报成功" in info:
            return True
        return False

    def cross_campus(self, cross_campus_data):
        data = self.login.session.get("https://weixine.ustc.edu.cn/2020").text
        soup = BeautifulSoup(data, "html.parser")
        headers = {
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39"
        }
        data = self.login.session.get("https://weixine.ustc.edu.cn/2020/apply/daliy/i?t=3",headers=headers).text
        data = data.encode("ascii", "ignore").decode("utf-8", "ignore")
        soup = BeautifulSoup(data, "html.parser")
        token = soup.find("input", {"name": "_token"})["value"]
        start_date = soup.find("input", {"id": "start_date"})["value"]
        end_date = soup.find("input", {"id": "end_date"})["value"]
        data = cross_campus_data + [
            ("_token", token),
            ("start_date", start_date),
            ("end_date", end_date),
            ("t", "3"),
        ]
        post = self.login.session.post("https://weixine.ustc.edu.cn/2020/apply/daliy/ipost",data=data)
        if "?t=d" in post.url:
            print("跨校区报备：成功")
            return True
        print("跨校区报备：失败")
        return False

    def out_school(self, out_school_data):
        data = self.login.session.get("https://weixine.ustc.edu.cn/2020").text
        soup = BeautifulSoup(data, "html.parser")
        headers = {
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39"
        }
        data = self.login.session.get("https://weixine.ustc.edu.cn/2020/apply/daliy/i?t=2",headers=headers).text
        data = data.encode("ascii", "ignore").decode("utf-8", "ignore")
        soup = BeautifulSoup(data, "html.parser")
        token = soup.find("input", {"name": "_token"})["value"]
        start_date = soup.find("input", {"id": "start_date"})["value"]
        end_date = soup.find("input", {"id": "end_date"})["value"]
        data = out_school_data + [
            ("_token", token),
            ("start_date", start_date),
            ("end_date", end_date),
            ("t", "2"),
        ]
        post = self.login.session.post(
            "https://weixine.ustc.edu.cn/2020/apply/daliy/ipost",
            data=data)
        if "?t=d" in post.url:
            print("出校报备：成功")
            return True
        print("出校报备：失败")
        return False
