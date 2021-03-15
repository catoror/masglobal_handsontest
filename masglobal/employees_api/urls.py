from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'get_employees/', views.EmployeeAPIView.as_view(), name="api_get_employees"),
]
