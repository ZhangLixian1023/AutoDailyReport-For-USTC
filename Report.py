from bs4 import BeautifulSoup
from ustclogin import Login


class Report(object):
    def __init__(self, stuid, password):
        self.stuid = stuid
        self.password = password
        self.login = Login(self.stuid, self.password,"https://weixine.ustc.edu.cn/2020/caslogin")

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