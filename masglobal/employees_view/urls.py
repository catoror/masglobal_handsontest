from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'get_employees/', views.EmployeeHTMLView.as_view(), name="get_employees"),
]
