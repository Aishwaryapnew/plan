
from django.shortcuts import render, redirect,get_object_or_404
from .models import ExamComponent
from django.http import HttpResponse

def exam_table(request):
    components = ExamComponent.objects.all()
    return render(request, 'assis.html', {'components': components})

def assessment_plan_view(request):
    if request.method == 'POST':
        # Retrieve form data
        vmid_duration = request.POST.get('mid_duration')
        vflexible_duration = request.POST.get('flexible_duration')
        vend_duration = request.POST.get('end_duration')

        vmid_weightage = request.POST.get('mid_weightage')
        vflexible_weightage = request.POST.get('flexible_weightage')
        vend_weightage = request.POST.get('end_weightage')

        vmid_typology = request.POST.get('mid_typology')
        vflexible_typology = request.POST.get('flexible_typology')
        vend_typology = request.POST.get('end_typology')

        vmid_pattern = request.POST.get('mid_pattern')
        vflexible_pattern = request.POST.get('flexible_pattern')
        vend_pattern = request.POST.get('end_pattern')

        vmid_schedule = request.POST.get('mid_schedule')
        vflexible_schedule = request.POST.get('flexible_schedule')
        vend_schedule = request.POST.get('end_schedule')

        vmid_topics = request.POST.get('mid_topics')
        vflexible_topics = request.POST.get('flexible_topics')
        vend_topics = request.POST.get('end_topics')

        ExamComponent.objects.create(
            component='Mid Sem Exam',
            duration=vmid_duration,
            weightage=vmid_weightage,
            typology_of_questions=vmid_typology,
            pattern=vmid_pattern,
            schedule=vmid_schedule,
            topics_covered=vmid_topics
        )

        # For Flexible Assessments
        ExamComponent.objects.create(
            component='Flexible Assessments',
            duration=vflexible_duration,
            weightage=vflexible_weightage,
            typology_of_questions=vflexible_typology,
            pattern=vflexible_pattern,
            schedule=vflexible_schedule,
            topics_covered=vflexible_topics
        )

        # For End Semester/Makeup Examination
        ExamComponent.objects.create(
            component='End Semester/Makeup Examination',
            duration=vend_duration,
            weightage=vend_weightage,
            typology_of_questions=vend_typology,
            pattern=vend_pattern,
            schedule=vend_schedule,
            topics_covered=vend_topics
        )

        return HttpResponse("Assessment Plan Submitted Successfully!")
    
    return render(request, 'viewuser.html')  # Or your existing template

def viewuser(request):
    user=ExamComponent.objects.all()
    return render(request,"viewuser.html",{'userdata':user})

def deleteprofile(request,id):
    user=ExamComponent.objects.get(id=id)
    user.delete()    
    return redirect("viewuser")

def edit(request,id):
    user=ExamComponent.objects.get(id=id)
    return render(request, "edit.html",{'userdata':user})

def updateprofile(request, id):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')  # Get which form was submitted

        # Retrieve the ExamComponent object using the id
        user = get_object_or_404(ExamComponent, id=id)
        
        if form_type == 'mid_sem_form':
            # Update values for Mid Sem Exam
            user.duration = request.POST.get('mid_duration', user.duration)
            user.weightage = request.POST.get('mid_weightage', user.weightage)
            user.typology_of_questions = request.POST.get('mid_typology', user.typology_of_questions)
            user.pattern = request.POST.get('mid_pattern', user.pattern)
            user.schedule = request.POST.get('mid_schedule', user.schedule)
            user.topics_covered = request.POST.get('mid_topics', user.topics_covered)
            user.save()

        elif form_type == 'flexible_assessment_form':
            # Retrieve or update Flexible Assessment
            flexible_assessment, created = ExamComponent.objects.get_or_create(component='Flexible Assessments', defaults={
                'duration': request.POST.get('flexible_duration', ''),
                'weightage': request.POST.get('flexible_weightage', ''),
                'typology_of_questions': request.POST.get('flexible_typology', ''),
                'pattern': request.POST.get('flexible_pattern', ''),
                'schedule': request.POST.get('flexible_schedule', ''),
                'topics_covered': request.POST.get('flexible_topics', ''),
            })
            if not created:
                flexible_assessment.duration = request.POST.get('flexible_duration', flexible_assessment.duration)
                flexible_assessment.weightage = request.POST.get('flexible_weightage', flexible_assessment.weightage)
                flexible_assessment.typology_of_questions = request.POST.get('flexible_typology', flexible_assessment.typology_of_questions)
                flexible_assessment.pattern = request.POST.get('flexible_pattern', flexible_assessment.pattern)
                flexible_assessment.schedule = request.POST.get('flexible_schedule', flexible_assessment.schedule)
                flexible_assessment.topics_covered = request.POST.get('flexible_topics', flexible_assessment.topics_covered)
                flexible_assessment.save()

        elif form_type == 'end_sem_form':
            # Retrieve or update End Semester Assessment
            end_sem_exam, created = ExamComponent.objects.get_or_create(component='End Semester/Makeup Examination', defaults={
                'duration': request.POST.get('end_duration', ''),
                'weightage': request.POST.get('end_weightage', ''),
                'typology_of_questions': request.POST.get('end_typology', ''),
                'pattern': request.POST.get('end_pattern', ''),
                'schedule': request.POST.get('end_schedule', ''),
                'topics_covered': request.POST.get('end_topics', ''),
            })
            if not created:
                end_sem_exam.duration = request.POST.get('end_duration', end_sem_exam.duration)
                end_sem_exam.weightage = request.POST.get('end_weightage', end_sem_exam.weightage)
                end_sem_exam.typology_of_questions = request.POST.get('end_typology', end_sem_exam.typology_of_questions)
                end_sem_exam.pattern = request.POST.get('end_pattern', end_sem_exam.pattern)
                end_sem_exam.schedule = request.POST.get('end_schedule', end_sem_exam.schedule)
                end_sem_exam.topics_covered = request.POST.get('end_topics', end_sem_exam.topics_covered)
                end_sem_exam.save()

        # Redirect after successful update
        return redirect("viewuser")
    
    
    return render("viewuser")  # Or render the edit page if needed
