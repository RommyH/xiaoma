from club.testCase import xiaoma_club
from  unittest import  TestCase
from app.control import start_app,app_personalCenter_version,connect_device,timeout_time
class xiaoma_app(TestCase):
    def setUp(self):
        connect_device(self)
        timeout_time(self)

    def testcase001_personalCenter_version(self):
        start_app(self)
        assert app_personalCenter_version(self)