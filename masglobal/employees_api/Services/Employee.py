import abc

class Employee(abc.ABC):
    def __init__(self, employee_id, name, contract_type_name, role_id,
                 role_name, role_description, hourly_salary, monthly_salary):
        self.employee_id = employee_id
        self.name = name
        self.contract_type_name = contract_type_name
        self.role_id = role_id
        self.role_name = role_name
        self.role_description = role_description
        self.hourly_salary = hourly_salary
        self.monthly_salary = monthly_salary

    @abc.abstractmethod
    def calculate_anual_salary(self):
        pass
