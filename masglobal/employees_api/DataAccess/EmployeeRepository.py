import abc

class EmployeeRepository(abc.ABC):
    def __init__(self, url):
        self.url = url

    @abc.abstractmethod
    def get_employees(self):
        pass

    @abc.abstractmethod
    def get_employees_by_id(self, id):
        pass
