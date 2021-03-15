from employees_api.Serializers.EmployeeSerializer import EmployeeSerializer
from employees_api.Services.Factory.EmployeeFactory import EmployeeFactory

class EmployeeJsonSerializer(EmployeeSerializer):
    def serialize(self, employee):
        json_employee = {
                'id' : employee.employee_id,
                'name' : employee.name,
                'contractTypeName' : employee.contract_type_name,
                'roleId' : employee.role_id,
                'roleName' : employee.role_name,
                'roleDescription' : employee.role_description,
                'hourlySalary' : employee.hourly_salary,
                'monthlySalary' : employee.monthly_salary,
                'calculatedAnualSalary' : employee.anual_salary
        }
        return json_employee
        
    class Meta:
    	model = EmployeeFactory
