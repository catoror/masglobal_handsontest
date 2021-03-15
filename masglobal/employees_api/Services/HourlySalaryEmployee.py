from employees_api.Services.Employee import Employee

class HourlySalaryEmployee(Employee):
    def __init__(self, employee_id, name, contract_type_name, role_id,
                 role_name, role_description, hourly_salary, monthly_salary):
        Employee.__init__(self, employee_id, name, contract_type_name, role_id,
                 role_name, role_description, hourly_salary, monthly_salary)
        self.anual_salary = self.calculate_anual_salary()

    def calculate_anual_salary(self):
        return 120 * self.hourly_salary * 12
