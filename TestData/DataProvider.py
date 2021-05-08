import datetime

from utilities import ReadConfig, ExcelUtil


class DataProvider:
    @staticmethod
    def get_test_data(sheet):
        data_list = []
        file_path = ReadConfig.ReadConfig.get_test_data_excel_path()

        if sheet == 'Test_data_for_login':
            test_sheet = ReadConfig.ReadConfig.get_sheet_name_for_login()
            f_name = "login"
            row_count = ExcelUtil.get_rowcount(file_path, test_sheet)
            for i in range(7, row_count, 3):  # to get rows
                dict = {}
                dict['username'] = ExcelUtil.read_data(file_path, test_sheet, i, 4)
                dict['password'] = ExcelUtil.read_data(file_path, test_sheet, i + 1, 4)
                dict['row_num'] = i

                now = datetime.datetime.now()
                date_time = now.strftime("%m-%d-%Y,%H-%M-%S")
                sheet_name = "TR-" + f_name + "-" + date_time
                dict['sheet_name'] = sheet_name

                data_list.append(dict)

        destination_file = ReadConfig.ReadConfig.get_test_report_excel_path()
        mr = ExcelUtil.get_rowcount(file_path, test_sheet)
        mc = ExcelUtil.get_col_count(file_path, test_sheet)

        ExcelUtil.create_sheet(destination_file, sheet_name)

        for i in range(1, mr + 1):
            for j in range(1, mc + 1):
                # reading cell value from source excel file
                c = ExcelUtil.read_data(file_path, test_sheet, i, j)

                # writing the read value to destination excel file
                if c is not None:
                    ExcelUtil.write_data(destination_file, sheet_name, i, j, c)

        return data_list

