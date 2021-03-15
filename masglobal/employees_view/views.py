from django.shortcuts import render
from django.views.generic import FormView


from employees_view.Forms.EmployeeForm import EmployeeForm

# Create your views here.

class EmployeeHTMLView(FormView):
    template_name = 'employees/get_employees.html'
    form_class = EmployeeForm
    success_url = '.'

    def form_valid(self, form):
        return super().form_valid(form)
