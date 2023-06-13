
from django.urls import re_path,path
from first_app import views
from django.contrib import admin

urlpatterns = [
   #re_path(r'^$', views.student, name='student'),
    re_path(r'^$', views.index, name='index'),
    path('student/',views.student,name='student'),
    path('faculty/',views.faculty,name='faculty'),
    path('EWUadmin/',views.EWUadmin,name='EWUadmin'),
    path("student/login/", views.login_request, name="login"),
    path('login/',views.login_request,name='login'),
    path('grade_submit/',views.grade_sub,name='grade_submit'),
    path('grade_rep/',views.grade_report,name='grade_rep'),
    path('login/StudentPage/topic_reg/',views.topic_registration,name='topic_reg'),
    path('login/StudentPage/meeting_sch/',views.meeting_list,name='meeting_sch'),
    path('faculty/loggin/facultyPage/grp_list/',views.all_grp,name='grp_list'),
    path('faculty/loggin/facultyPage/meeting/',views.meeting_set,name='meeting'),
    path('faculty/loggin/facultyPage/grade_submit/',views.grade_sub,name='grade-submit'),
    path('admin/', admin.site.urls),
    path('student/login/StudentPage/',views.StudentPage,name='StduentPage'),
    path('student/student/login/',views.login,name='StduentPage'),

    path('login/StudentPage/',views.StudentPage,name='StduentPage'),
    path('faculty/loggin/',views.login,name='faculty'),
    path('loggin/',views.login,name='login'),
    path("sign/", views.admin_signup, name="sign"),
    path("addFaculty/", views.addfaculty, name="addf"),
    path('EWUadmin/sign/',views.adninpanel,name='admin'),
    path('EWUadmin/sign/sign/',views.admin_signup,name='admin'),
    path('EWUadmin/sign/sign/adminPage/',views.admin1,name='admin'),
    path('EWUadmin/sign/sign/adminPage/addfaculty',views.addfaculty,name='admin'),
    path('admin/',views.admin1,name='admin'),
    path('faculty/faculty/loggin/',views.login,name='faculty'),
    path('faculty/loggin/facultyPage/',views.FacultyPage,name='faculty'),
    path('faculty/faculty/loggin/facultyPage/',views.FacultyPage,name='faculty'),
    path('/faculty/loggin/facultyPage/grp_list/',views.all_grp,name='faculty'),
    path('EWUadmin/sign/sign/adminPage/viewGroup/',views.all_grp,name='admin'),
    #path('EWUadmin/sign/sign/adminPage/addfaculty/',views.Addfaculty,name='admin'),
    path('addfaculty/',views.Addfaculty,name='addfaculty'),
    
    
     
    #path("register/", views.register, name="register")
    #path('index/',views.index,name='index'),

]
