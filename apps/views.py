
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
        # Get values for Mid Sem Exam
        vmid_duration = request.POST['mid_duration']
        vmid_weightage = request.POST['mid_weightage']
        vmid_typology = request.POST['mid_typology']
        vmid_pattern = request.POST['mid_pattern']
        vmid_schedule = request.POST['mid_schedule']
        vmid_topics = request.POST['mid_topics']

        # Get values for Flexible Assessments
        vflexible_duration = request.POST['flexible_duration']
        vflexible_weightage = request.POST['flexible_weightage']
        vflexible_typology = request.POST['flexible_typology']
        vflexible_pattern = request.POST['flexible_pattern']
        vflexible_schedule = request.POST['flexible_schedule']
        vflexible_topics = request.POST['flexible_topics']

        # Get values for End Semester/Makeup Examination
        vend_duration = request.POST['end_duration']
        vend_weightage = request.POST['end_weightage']
        vend_typology = request.POST['end_typology']
        vend_pattern = request.POST['end_pattern']
        vend_schedule = request.POST['end_schedule']
        vend_topics = request.POST['end_topics']

        # Retrieve the ExamComponent object using the id for the Mid Sem Exam
        user = get_object_or_404(ExamComponent, id=id)
        user.duration = vmid_duration
        user.weightage = vmid_weightage
        user.typology_of_questions = vmid_typology
        user.pattern = vmid_pattern
        user.schedule = vmid_schedule
        user.topics_covered = vmid_topics
        user.save()
       
        # Update Flexible Assessments
        ExamComponent.objects.create(
            component='Flexible Assessments',
            duration=vflexible_duration,
            weightage=vflexible_weightage,
            typology_of_questions=vflexible_typology,
            pattern=vflexible_pattern,
            schedule=vflexible_schedule,
            topics_covered=vflexible_topics
        )
       
        # Update End Semester/Makeup Examination
        ExamComponent.objects.create(
            component='End Semester/Makeup Examination',
            duration=vend_duration,
            weightage=vend_weightage,
            typology_of_questions=vend_typology,
            pattern=vend_pattern,
            schedule=vend_schedule,
            topics_covered=vend_topics
        )

        # Redirect after successful update
        return redirect("viewuser")
    
    return render("viewuser")  # Or render the edit page if needed
