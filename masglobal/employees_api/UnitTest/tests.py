from django.test import TestCase

from employees_api.Services.Factory.EmployeeFactory import EmployeeFactory

# Create your tests here.


class TestEmployeeFactory(TestCase):
	def test_hourly_salary_type(self):
		
		obj_employee = {'id': 3, 'name': 'Maria', 
		                'contractTypeName': 'HourlySalaryEmployee', 
		                'roleId': 1, 'roleName': 'Administrator', 
		                'roleDescription': None, 'hourlySalary': '12-5', 
		                'monthlySalary': 50000.0}

		obj_employee_factory = EmployeeFactory()
		self.assertRaises(TypeError, 
                          obj_employee_factory.create_employee(obj_employee))

	def test_monthly_salary_type(self):
		
		obj_employee = {'id': 4, 'name': 'Adriana', 
		                'contractTypeName': 'HourlySalaryEmployee', 
		                'roleId': 2, 'roleName': 'Contractor', 
		                'roleDescription': None, 'hourlySalary': 5000.0, 
		                'monthlySalary': 404.0}

		obj_employee_factory = EmployeeFactory()
		self.assertRaises(TypeError, 
                          obj_employee_factory.create_employee(obj_employee))


	def test_existing_contract_type(self):
		
		obj_employee = {'id': 5, 'name': 'Daniel', 
		                'contractTypeName': 'WeeklySalaryEmployee', 
		                'roleId': 3, 'roleName': 'Developer', 
		                'roleDescription': None, 'hourlySalary': 5000.0, 
		                'monthlySalary': 50000.0}

		obj_employee_factory = EmployeeFactory()
		self.assertRaises(ValueError, 
                          obj_employee_factory.create_employee(obj_employee))

	def test_hourly_salary_anual_value(self):
		
		obj_employee = {'id': 6, 'name': 'Carlos', 
		                'contractTypeName': 'HourlySalaryEmployee', 
		                'roleId': 1, 'roleName': 'Administrator', 
		                'roleDescription': None, 'hourlySalary': 1000.0, 
		                'monthlySalary': 50000.0}

		obj_employee_factory = EmployeeFactory()
		employee = obj_employee_factory.create_employee(obj_employee)
		self.assertEqual(employee.anual_salary, 1440000)


	def test_monthly_salary_anual_value(self):
		
		obj_employee = {'id': 7, 'name': 'Andres', 
		                'contractTypeName': 'MonthlySalaryEmployee', 
		                'roleId': 2, 'roleName': 'Contractor', 
		                'roleDescription': None, 'hourlySalary': 5000.0, 
		                'monthlySalary': 400000.0}

		obj_employee_factory = EmployeeFactory()
		employee = obj_employee_factory.create_employee(obj_employee)
		self.assertEqual(employee.anual_salary, 4800000)

	def test_monthly_salary_anual_value_wrong(self):
		
		obj_employee = {'id': 7, 'name': 'Andres', 
		                'contractTypeName': 'MonthlySalaryEmployee', 
		                'roleId': 2, 'roleName': 'Contractor', 
		                'roleDescription': None, 'hourlySalary': 5000.0, 
		                'monthlySalary': 400000.0}

		obj_employee_factory = EmployeeFactory()
		employee = obj_employee_factory.create_employee(obj_employee)
		self.assertEqual(employee.anual_salary, 4900000)


	def test_monthly_salary_anual_value_not_equal(self):
		
		obj_employee = {'id': 7, 'name': 'Andres', 
		                'contractTypeName': 'MonthlySalaryEmployee', 
		                'roleId': 2, 'roleName': 'Contractor', 
		                'roleDescription': None, 'hourlySalary': 5000.0, 
		                'monthlySalary': 400000.0}

		obj_employee_factory = EmployeeFactory()
		employee = obj_employee_factory.create_employee(obj_employee)
		self.assertNotEqual(employee.anual_salary, 4900000)


	def test_monthly_salary_anual_value_not_equal_wrong(self):
		
		obj_employee = {'id': 7, 'name': 'Andres', 
		                'contractTypeName': 'MonthlySalaryEmployee', 
		                'roleId': 2, 'roleName': 'Contractor', 
		                'roleDescription': None, 'hourlySalary': 5000.0, 
		                'monthlySalary': 400000.0}

		obj_employee_factory = EmployeeFactory()
		employee = obj_employee_factory.create_employee(obj_employee)
		self.assertNotEqual(employee.anual_salary, 4800000)
