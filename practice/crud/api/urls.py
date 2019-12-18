from django.contrib import admin
from django.urls import path,include
from  rest_framework import routers
from api.views import EmployeeViewSet
# routers=routers.DefaultRouter()
# routers.register('employee/',EmployeeViewSet)
from rest_framework.routers import DefaultRouter
from api import views
router = DefaultRouter()
router.register('',EmployeeViewSet)
urlpatterns =[
    path('employee/',include(router.urls)),
    path('poll/',views.Poll),
    path('poll_detail/<int:id>',views.Poll_Detail),
    path('emp_list/',views.Employee_list.as_view())
]

