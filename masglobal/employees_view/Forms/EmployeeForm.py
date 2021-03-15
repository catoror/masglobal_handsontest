# -*- coding: utf-8 -*-

from django.forms import Form, CharField, TextInput

class EmployeeForm(Form):
    id = CharField( widget=TextInput(attrs={'class':'form-control text-width','placeholder':u'Employee ID', 'type':'number', 'min':1}), required=False)
