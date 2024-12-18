from django import forms
from .models import ExamComponent
class AssessmentPlanForm(forms.ModelForm):
    class Meta:
        model = ExamComponent
        fields = ['component', 'duration', 'weightage', 'typology_of_questions',
                  'pattern', 'schedule', 'topics_covered']
