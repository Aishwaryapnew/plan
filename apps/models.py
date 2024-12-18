from django.db import models

class ExamComponent(models.Model):
    COMPONENT_CHOICES = [
        ('Mid Sem Exam', 'Mid Sem Exam'),
        ('Flexible Assessments', 'Flexible Assessments'),
        ('End Semester/Makeup Examination', 'End Semester/Makeup Examination'),
    ]

    component = models.CharField(max_length=50, choices=COMPONENT_CHOICES)
    
    # If duration and weightage are numeric, you may want to use IntegerField or DecimalField
    duration = models.CharField(max_length=50, help_text="Enter duration (e.g., 2 hours or 90 minutes)")
    weightage = models.CharField(max_length=50, help_text="Enter weightage (percentage)")
    
    # If you're storing the typology and pattern as descriptive text, the TextField is good
    typology_of_questions = models.TextField(help_text="Enter question typology")
    pattern = models.TextField(help_text="Describe the pattern")
    
    # The schedule could also be numeric, or a textual representation depending on your needs
    schedule = models.CharField(max_length=50, help_text="Enter schedule details")
    
    # Topics covered is fine as TextField for longer descriptions
    topics_covered = models.TextField(help_text="Enter topics covered")

    class Meta:
        db_table = 'datanew'