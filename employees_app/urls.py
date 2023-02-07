from django.urls import path
from .views import *  # import all views of employee-app

urlpatterns = [
    path('', homepage, name='homepage'),
    path('not/found-errors/', not_found_page, name='page_not_found'),
    path('search/employee/',search_employees, name='employeesFilter'),
    path('add-employee/',AddEmployeeView.as_view(), name='addEmployees'),
    path("update-employee/<int:id>/", AupdateEmployee.as_view(), name="update_employee"),
    path('delete-employee/<int:id>/',DeleteEmployee.as_view(), name='deleteEmployee'),

]
