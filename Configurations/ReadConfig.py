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

    @staticmethod
    def get_test_data_excel_path():
        excel_path = config.get('Excel info', 'excel_file_for_test_data')
        return excel_path

    @staticmethod
    def get_test_report_excel_path():
        excel_path = config.get('Excel info', 'excel_file_for_test_report')
        return excel_path

    @staticmethod
    def get_sheet_name_for_login():
        sheet_name = config.get('Excel info', 'sheet_name_for_login')
        return sheet_name

    @staticmethod
    def get_sheet_name_for_add_department():
        sheet_name = config.get('Excel info', 'sheet_name_for_add_department')
        return sheet_name

    @staticmethod
    def get_sheet_name_for_add_employee():
        sheet_name = config.get('Excel info', 'sheet_name_for_add_employee')
        return sheet_name
