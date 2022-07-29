from bs4 import BeautifulSoup
import requests
class Login:
    def __init__(self, stuid, password, service):
        self.stuid = stuid
        self.password = password
        self.service = service
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71',
            'Connection': 'keep-alive'
            }

    def login(self):
        # 建立会话
        s=requests.session()
        self.session=s
        s.trust_env = False
        # 添加header, 模拟浏览器, 避免被服务器当成脚本
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71',
            'Connection': 'keep-alive'
        }
        # 统一身份认证登录
        login_url='https://passport.ustc.edu.cn/login'
        r = s.get(login_url, params = {'service': self.service})
        CAS_LT=BeautifulSoup(r.text, 'html.parser').find('input', {'name':'CAS_LT'})['value']
        form_data = {
            'model': 'uplogin.jsp',
            'CAS_LT': CAS_LT,
            'service': self.service,
            'username': self.stuid,
            'password': self.password
        }
        self.result = s.post(login_url, data=form_data, headers=header)
        if self.result.url == "https://passport.ustc.edu.cn/login":
            print("登录健康平台：失败")
            exit(-1)
        else:
            print("登录健康平台：成功")
