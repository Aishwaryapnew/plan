from django.urls import path
from . import views

urlpatterns = [
    path('exam_table/', views.exam_table, name='exam_table'),
    path('assessment_plan_view/', views.assessment_plan_view, name='assessment_plan_view'),
]
