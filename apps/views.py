
from django.shortcuts import render, redirect, get_object_or_404
from .models import ExamComponent
from .forms import AssessmentPlanForm

def exam_table(request):
    components = ExamComponent.objects.all()
    return render(request, 'assis.html', {'components': components})

def assessment_plan_view(request):
    if request.method == 'POST':
        # Retrieve form data
        mid_duration = request.POST.get('mid_duration')
        flexible_duration = request.POST.get('flexible_duration')
        end_duration = request.POST.get('end_duration')

        mid_weightage = request.POST.get('mid_weightage')
        flexible_weightage = request.POST.get('flexible_weightage')
        end_weightage = request.POST.get('end_weightage')

        mid_typology = request.POST.get('mid_typology')
        flexible_typology = request.POST.get('flexible_typology')
        end_typology = request.POST.get('end_typology')

        mid_pattern = request.POST.get('mid_pattern')
        flexible_pattern = request.POST.get('flexible_pattern')
        end_pattern = request.POST.get('end_pattern')

        mid_schedule = request.POST.get('mid_schedule')
        flexible_schedule = request.POST.get('flexible_schedule')
        end_schedule = request.POST.get('end_schedule')

        mid_topics = request.POST.get('mid_topics')
        flexible_topics = request.POST.get('flexible_topics')
        end_topics = request.POST.get('end_topics')

        # Save data to the database
        ExamComponent.objects.create(
            mid_duration=mid_duration,
            flexible_duration=flexible_duration,
            end_duration=end_duration,
            mid_weightage=mid_weightage,
            flexible_weightage=flexible_weightage,
            end_weightage=end_weightage,
            mid_typology=mid_typology,
            flexible_typology=flexible_typology,
            end_typology=end_typology,
            mid_pattern=mid_pattern,
            flexible_pattern=flexible_pattern,
            end_pattern=end_pattern,
            mid_schedule=mid_schedule,
            flexible_schedule=flexible_schedule,
            end_schedule=end_schedule,
            mid_topics=mid_topics,
            flexible_topics=flexible_topics,
            end_topics=end_topics
        )

        return HttpResponse("Assessment Plan Submitted Successfully!")
    
    return render(request, 'viewuser.html')  # Or your existing template
