from django.urls import path
from . import views

urlpatterns = [
    path('exam_table/', views.exam_table, name='exam_table'),
    path('exam_table/assessment_plan_view/', views.assessment_plan_view, name='assessment_plan_view'),  
    path('viewuser/',views.viewuser,name='viewuser'),
    path('deleteprofile/<int:id>/',views.deleteprofile,name='deleteprofile'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('updateprofile/<int:id>/', views.updateprofile, name='updateprofile'),
]