from django.test import TestCase
from .forms import EmployeeForm, CreateUserForm
from .models import *
# Create your tests here.

class PositionModelTest(TestCase):
    
    def position_creation_test(self):
        position = Position.objects.create(title="test")
        self.assertTrue(isinstance(position, Position))
        self.assertEqual(position.__str__(), position.title)
    
    def position_update_test(self):
        position = Position.objects.create(title="test")
        position.title = "test1"
        position.save()
        self.assertEqual(position.title, "test1")
        
    def position_delete_test(self):
        position = Position.objects.create(title="test")
        position.delete()
        self.assertEqual(Position.objects.count(), 0)

class EmployeModelTest(TestCase):
    
    def employe_creation_test(self):
        """
        summary_: This test is for create the employee and 
        check the data is created or not with
        
        """
        employe = Employee.objects.create(fullname="test", mobile="1234567890", emp_code="123456", position=0)
        self.assertTrue(isinstance(employe, Employee))
        self.assertEqual(employe.__str__(), employe.fullname)
    
    def employe_update_test(self):
        """_
        summary_: This test is for update the employee 
        data and check the data is updated or not with
        the help of assertEqual and negative test case negative foreig key
        """
        employe = Employee.objects.create(fullname="test", mobile="1234567890", emp_code="123456", position=-1)
        employe.fullname = "test1"
        employe.save()
        self.assertEqual(employe.fullname, "test1")
        
    def employe_delete_test(self):
        """
        test for delete the employee data and check the data is deleted or not with
        """
        employe = Employee.objects.create(fullname="test", mobile="1234567890", emp_code="123456", position="test")
        employe.delete()
        self.assertEqual(Employee.objects.count(), 0)
    
#test the employes form

def test_EmployeeForm():
    assert EmployeeForm
    
def test_CreateUserForm():
    assert CreateUserForm