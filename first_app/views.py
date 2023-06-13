from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Student 
from .models import Faculty
from .models import ProposedTopic
from .models import MeetingTable
from .models import GradeTable
from .models import Ad_panel

 
def index(request):
    diction = {'title':"Index"}
    return render(request, 'first_app/index.html', context=diction)

def student_form(request):
    diction = {}
    return render(request, 'first_app/student_form.html', context=diction)


def student (request):
     user=Student.objects.all()
     if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        #contact,gender,address are not included
        if Student.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already exists.')
            return redirect('login/')
        elif Student.objects.filter(userName=username).exists():
            messages.warning(request, 'Username is already exists.')
            return redirect('login/')
        else:
            add_student=Student(first_name=firstname,last_name=lastname,userName=username,email=email,phone=contact,password=password)
            add_student.save()
            #add_student.set_password(password)
            #add_student.save()

            add_student=Student()
            add_student=user
            add_student.contact=contact
            #data.email=email
            #add_student.save()
            messages.success(request, 'New user has been registered successfully.')
            return redirect('student/login/')
	
     return render(request,'first_app/student_form.html')

def faculty (request) :
    user=Faculty.objects.all()
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if Faculty.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already exists.')
            return redirect('loggin/')
        elif Faculty.objects.filter(userName=username).exists():
            messages.warning(request, 'Username is already exists.')
            return redirect('loggin/')
        else:
            add_faculty=Faculty(first_name=firstname,last_name=lastname,userName=username,email=email,password=password)
            add_faculty.save()
            add_faculty=Student()
            add_faculty=user
            messages.success(request, 'New user has been registered successfully.')
            return redirect('faculty/loggin/')
    return render(request,'first_app/faculty.html')

def adninpanel (request) :
    user=Ad_panel.objects.all()
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        add_adminpanel=Ad_panel(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
        add_adminpanel.save()
        add_adminpanel=Ad_panel()
        add_adminpanel=user
                    
        messages.success(request, 'New user has been registered successfully.')
        return redirect('EWUadmin/sign/')
    return render(request,'first_app/EWUAdmin.html')

def EWUadmin (request) :
    return render(request,'first_app/EWUAdmin.html')

def StudentPage (request):
    return render(request,'first_app/student_page.html')
def FacultyPage (request):
    return render(request,'first_app/faculty_page.html')
def admin1 (request) :
    return render(request,'first_app/admin.html')

def Addfaculty (request):
    return render(request,'first_app/add_faculty.html')

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def login_request(request):
    user=Student.objects.all()
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if(Student.objects.filter(userName=username)):
            if(Student.objects.filter(password=password)):
                #request.session['name'] = email
                return redirect('StudentPage/')
            else:
               
                return render(request,'first_app/login.html')
        else:
           
            return render(request,'first_app/login.html')
    return render(request,'first_app/login.html')
def login(request):
    user=Faculty.objects.all()
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if(Faculty.objects.filter(userName=username)):
            if(Faculty.objects.filter(password=password)):
                #request.session['name'] = email
                return redirect('facultyPage/')
            else:
               
                return render(request,'first_app/login.html')
        else:
           
            return render(request,'first_app/login.html')
    return render(request,'first_app/login.html')

def topic_registration (request):
    if request.method=='POST':
        topicname=request.POST.get('topicName')
        member1=request.POST.get('mem1')
        member2=request.POST.get('mem2')
        member3=request.POST.get('mem3')
        paper1=request.POST.get('pap1')
        paper2=request.POST.get('pap2')
        paper3=request.POST.get('pap3')
        paper4=request.POST.get('pap4')
        paper5=request.POST.get('pap5')

        data=ProposedTopic()
        data.topicname=topicname
        data.member1=member1
        data.member2=member2
        data.member3=member3
        data.paper1=paper1
        data.paper2=paper2
        data.paper3=paper3
        data.paper4=paper4
        data.paper5=paper5

        data.save()
    return render(request,'first_app/proposed_topic.html')

def all_grp (request):
    grp=ProposedTopic.objects.all()
    context={
        'data':grp,
    }
    return render(request,'first_app/group_list.html',context)

def meeting_set (request):
    if request.method=='POST':
        topicname=request.POST.get('topicName')
        date=request.POST.get('date')
        time=request.POST.get('time')
        room=request.POST.get('room')

        data1=MeetingTable()
        data1.topicname=topicname
        data1.date=date
        data1.time=time
        data1.room=room
        data1.save()
    return render(request,'first_app/meeting_setup.html')

def meeting_list (request):
    meet=MeetingTable.objects.all()
    context={
        'data':meet,
    }
    return render(request,'first_app/meeting_schedule.html',context)

def grade_sub (request):
    if request.method=='POST':
        topicname=request.POST.get('topicName')
        credit=request.POST.get('credit')
        grade=request.POST.get('grade')
        gpa=request.POST.get('gpa')

        data1=GradeTable()
        data1.topicname=topicname
        data1.credit=credit
        data1.grade=grade
        data1.gpa=gpa
        data1.save()
    return render(request,'first_app/grade_submit.html')

def grade_report (request):
    meet=GradeTable.objects.all()
    context={
        'data':meet,
    }
    return render(request,'first_app/grade_report.html',context)

def admin_signup(request):
    user=Ad_panel.objects.all()
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if(Ad_panel.objects.filter(userName=username)):
            if(Ad_panel.objects.filter(password=password)):
                #request.session['name'] = email
                return redirect('adminPage/')
            else:
               
                return render(request,'first_app/login.html')
        else:
           
            return render(request,'first_app/login.html')
    return render(request,'first_app/login.html')

def addfaculty (request) :
    user=Faculty.objects.all()
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if Faculty.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already exists.')
            return redirect('loggin/')
        elif Faculty.objects.filter(userName=username).exists():
            messages.warning(request, 'Username is already exists.')
            return redirect('loggin/')
        else:
            add_faculty=Faculty(first_name=firstname,last_name=lastname,userName=username,email=email,password=password)
            add_faculty.save()
            add_faculty=Student()
            add_faculty=user
            messages.success(request, 'New user has been registered successfully.')
            return redirect('faculty/loggin/')
    return render(request,'first_app/faculty.html')

from django.contrib.auth.models import User
from django.shortcuts import render

def your_view(request):
    student_object = Student.objects.get('fname')
    context = {'user_object': student_object}
    return render(request, 'first_app/student_form.html', context)





