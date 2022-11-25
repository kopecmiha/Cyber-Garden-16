from django.urls import path
from .views import CreateDepartment, DeleteDepartment, GetDepartments, AddToDepartment

urlpatterns = [
    path('create_department/', CreateDepartment.as_view()),
    path('delete_department/', DeleteDepartment.as_view()),
    path('get_departments/', GetDepartments.as_view()),
    path('add_to_department/', AddToDepartment.as_view()),

]