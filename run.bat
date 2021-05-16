pytest -v -s --alluredir="Reports"  TestCases/test_employee.py --browser chrome

pytest -v -s TestCases/test_department.py --browser chrome

allure serve Reports
