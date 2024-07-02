import configparser

config = configparser.ConfigParser()
config_file_path = "C:\\Users\Dev Patel\PycharmProjects\pythonWithSelenium\Configurations\config.ini"
config.read(config_file_path)


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get("common info", "baseURL")
        return url

    @staticmethod
    def getUserEmail():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
