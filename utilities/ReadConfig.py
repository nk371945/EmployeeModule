import configparser

config = configparser.RawConfigParser()
config.read("Configurations/config.ini")


class ReadConfig:

    @staticmethod
    def get_application_url():
        url = config.get('common info', 'url')
        return url

    @staticmethod
    def get_valid_login_email():
        email = config.get('common info', 'valid_login_email')
        return email

    @staticmethod
    def get_valid_login_password():
        password = config.get('common info', 'valid_login_password')
        return password
