import time
import configparser


class XiaoMaUtils(object):
    def __init__(self):
        pass

    """
        获取系统当前时间
        返回一个字符串类型
    """

    @classmethod
    def get_current_time(cls):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        return current_time

    """
        读取配置文件
        返回一个元组类型
    """

    @staticmethod
    def read_config(config_file):
        config = configparser.ConfigParser()
        config.read('config/' + config_file, encoding="utf-8-sig")
        project_name = config.get('config', 'project_name')
        app_name = config.get('config', 'app_name')
        app_version = config.get('config', 'app_version')

        return project_name, app_name, app_version


if __name__ == '__main__':
    pass
