from HTMLTestReportCN import HTMLTestRunner
from club.XiaoMaUtils import XiaoMaUtils
from unittest import makeSuite,TestSuite
from club.testCase import xiaoma_club
from app.testCase import xiaoma_app
suite=TestSuite()
suite.addTest(makeSuite(xiaoma_club))
suite.addTest(makeSuite(xiaoma_app))
# 读取配置文件
app_info = XiaoMaUtils.read_config("xiaoma_FL_club.ini")
project_name = app_info[0]
app_name = app_info[1]
app_version = app_info[2]

# 生成报告的标题
title = project_name + " " + app_name + " " + app_version + "版本 自动化测试报告"
Report = open("report/" + project_name + "_" + app_name + "_" + app_version + "版本_自动化测试报告_" + XiaoMaUtils.get_current_time().replace(":", "-") + ".html", "wb")
report = HTMLTestRunner(stream=Report, title=title)
report.run(suite)
Report.close()