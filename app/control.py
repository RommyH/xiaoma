import uiautomator2 as u2
from time import sleep
def connect_device(self):
    self.d=u2.connect('127.0.0.1:7555')  #连接pad

def timeout_time(self):
    self.d.wait_timeout = 6.0   #设置默认等待时间
    self.d.click_post_delay =1.0  #设置点击后1.5秒才能点击

def start_app(self):
    self.d.app_start('com.xiaoma.app')  #打开车应用
    sleep(3)

def app_personalCenter_version(self):
    personalCenter_text=self.d(resourceId="com.xiaoma.app:id/tv_app_name").info['text']
    personalCenter_version=self.d(resourceId="com.xiaoma.app:id/tv_version_number").info['text']
    if personalCenter_text == '车应用' and personalCenter_version == '版本：4.2.1.12':
        return True
    else:
        return False