import abc

class EmployeeSerializer(abc.ABC):
    @abc.abstractmethod
    def serialize(self, employee):
        pass

