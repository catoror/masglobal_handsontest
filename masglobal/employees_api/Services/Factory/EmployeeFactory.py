from employees_api.Services.HourlySalaryEmployee import HourlySalaryEmployee
from employees_api.Services.MonthlySalaryEmployee import MonthlySalaryEmployee

class EmployeeFactory:
    def create_employee(self, object_employee): 
        if not isinstance(object_employee['hourlySalary'], int) and \
           not isinstance(object_employee['hourlySalary'], float):
            raise TypeError("The value {0} is not a number".format(
            object_employee['hourlySalary']))

        if not isinstance(object_employee['monthlySalary'], int) and \
           not isinstance(object_employee['monthlySalary'], float):
            raise TypeError("The value {0} is not a number".format(
            object_employee['monthlySalary']))

        if object_employee['contractTypeName'] == 'HourlySalaryEmployee':
            return HourlySalaryEmployee(object_employee['id'], 
                                        object_employee['name'], 
                                        object_employee['contractTypeName'], 
                                        object_employee['roleId'], 
                                        object_employee['roleName'], 
                                        object_employee['roleDescription'], 
                                        object_employee['hourlySalary'],
                                        object_employee['monthlySalary'])
        elif object_employee['contractTypeName'] == 'MonthlySalaryEmployee':
            return MonthlySalaryEmployee(object_employee['id'], 
                                        object_employee['name'], 
                                        object_employee['contractTypeName'], 
                                        object_employee['roleId'], 
                                        object_employee['roleName'], 
                                        object_employee['roleDescription'], 
                                        object_employee['hourlySalary'],
                                        object_employee['monthlySalary'])
        else:
            raise ValueError("The type {0} is not a valid type".format(
            object_employee['contractTypeName']))
