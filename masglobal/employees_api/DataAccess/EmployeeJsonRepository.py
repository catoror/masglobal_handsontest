import requests
from employees_api.DataAccess.EmployeeRepository import EmployeeRepository
from employees_api.Services.Factory.EmployeeFactory import EmployeeFactory

class EmployeeJsonRepository(EmployeeRepository):
    def __init__(self, url):
        self.url = url

    def get_employees(self):
        url = self.url
        employee_request = requests.get(url)
        employees = employee_request.json()
        list_dto_employee = list(map(lambda employee : 
            EmployeeFactory().create_employee(employee), employees))
        return list_dto_employee

    def get_employees_by_id(self, id):
        url = self.url
        employee_request = requests.get(url)
        employees = employee_request.json()
        list_dto_employee = list(filter(None, map(lambda employee : 
			EmployeeFactory().create_employee(employee)
            if int(employee['id']) == int(id)
            else None,
            employees)))
        return list_dto_employee
