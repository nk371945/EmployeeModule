import datetime

from utilities import ReadConfig, ExcelUtil


class TestData:
    @staticmethod
    def getTestData(sheet):
        dataList = []
        filePath = ReadConfig.getValues('excelFilePath')

        if sheet == 'Test Data For Login':
            testSheet = ReadConfig.getValues('login_test_data')
            fname = "login"
            rowCount = ExcelUtil.get_rowcount(filePath, testSheet)
            for i in range(7, rowCount, 3):  # to get rows
                Dict = {}
                Dict['username'] = ExcelUtil.read_data(filePath, testSheet, i, 4)
                Dict['password'] = ExcelUtil.read_data(filePath, testSheet, i + 1, 4)
                Dict['rowNum'] = i

                now = datetime.datetime.now()
                date_time = now.strftime("%m-%d-%Y,%H")
                sheet_name = "TR-" + fname + "-" + date_time
                Dict['sheet_name'] = sheet_name

                dataList.append(Dict)

        elif sheet == 'Test_data_for_department':
            testSheet = ReadConfig.getValues('department')
            fname = "department"
            rowCount = ExcelUtil.get_rowcount(filePath, testSheet)
            for i in range(4, rowCount, 4):  # to get rows
                Dict = {}
                Dict['dept_name'] = ExcelUtil.read_data(filePath, testSheet, i, 4)
                Dict['parent_dept_name'] = ExcelUtil.read_data(filePath, testSheet, i + 1, 4)
                Dict['manager_name'] = ExcelUtil.read_data(filePath, testSheet, i + 2, 4)
                Dict['rowNum'] = i

                now = datetime.datetime.now()
                date_time = now.strftime("%m-%d-%Y,%H")
                sheet_name = "TR-" + fname + "-" + date_time
                Dict['sheet_name'] = sheet_name

                dataList.append(Dict)

        elif sheet == 'Test_data_for_employee':
            testSheet = ReadConfig.getValues('employee')
            fname = "employee"
            rowCount = ExcelUtil.get_rowcount(filePath, testSheet)
            for i in range(4, rowCount, 10):  # to get rows
                Dict = {}
                Dict['employee_name'] = ExcelUtil.read_data(filePath, testSheet, i, 4)
                Dict['employee_type'] = ExcelUtil.read_data(filePath, testSheet, i + 1, 4)
                Dict['work_address'] = ExcelUtil.read_data(filePath, testSheet, i + 2, 4)
                Dict['work_loc'] = ExcelUtil.read_data(filePath, testSheet, i + 3, 4)
                Dict['email'] = ExcelUtil.read_data(filePath, testSheet, i + 4, 4)
                Dict['mobile'] = ExcelUtil.read_data(filePath, testSheet, i + 5, 4)
                Dict['dept'] = ExcelUtil.read_data(filePath, testSheet, i + 6, 4)
                Dict['job_position'] = ExcelUtil.read_data(filePath, testSheet, i + 7, 4)
                Dict['manager'] = ExcelUtil.read_data(filePath, testSheet, i + 8, 4)
                Dict['rowNum'] = i

                now = datetime.datetime.now()
                date_time = now.strftime("%m-%d-%Y,%H")
                sheet_name = "TR-" + fname + "-" + date_time
                Dict['sheet_name'] = sheet_name

                dataList.append(Dict)

        elif sheet == 'Test_data_for_payroll':
            testSheet = ReadConfig.getValues('payroll')
            fname = "payroll"
            rowCount = ExcelUtil.get_rowcount(filePath, testSheet)
            for i in range(4, rowCount, 6):  # to get rows
                Dict = {}
                Dict['emp_name'] = ExcelUtil.read_data(filePath, testSheet, i, 4)
                Dict['from_date'] = ExcelUtil.read_data(filePath, testSheet, i + 1, 4)
                Dict['to_date'] = ExcelUtil.read_data(filePath, testSheet, i + 2, 4)
                Dict['structure'] = ExcelUtil.read_data(filePath, testSheet, i + 3, 4)
                Dict['rowNum'] = i

                now = datetime.datetime.now()
                date_time = now.strftime("%m-%d-%Y,%H")
                sheet_name = "TR-" + fname + "-" + date_time
                Dict['sheet_name'] = sheet_name

                dataList.append(Dict)

        elif sheet == 'Test_data_for_view_payslip':
            testSheet = ReadConfig.getValues('view_payslip')
            fname = "payslip"
            rowCount = ExcelUtil.get_rowcount(filePath, testSheet)
            for i in range(4, rowCount, 2):  # to get rows
                Dict = {}
                Dict['name'] = ExcelUtil.read_data(filePath, testSheet, i, 4)
                Dict['rowNum'] = i

                now = datetime.datetime.now()
                date_time = now.strftime("%m-%d-%Y,%H")                             #-%M-%S
                sheet_name = "TR-" + fname + "-" + date_time
                Dict['sheet_name'] = sheet_name

                dataList.append(Dict)


        destination_file = ReadConfig.getValues('test_report_file')
        mr = ExcelUtil.get_rowcount(filePath, testSheet)
        mc = ExcelUtil.get_col_count(filePath, testSheet)

        ExcelUtil.create_sheet(destination_file, sheet_name)

        for i in range(1, mr + 1):
            for j in range(1, mc + 1):
                # reading cell value from source excel file
                c = ExcelUtil.read_data(filePath, testSheet, i, j)

                # writing the read value to destination excel file

                if c is not None:
                    ExcelUtil.write_data(destination_file, sheet_name, i, j, c)

        return dataList

