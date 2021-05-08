pytest -v -s --alluredir="Reports"  TestCases/test_employee.py --browser chrome

allure serve Reports
