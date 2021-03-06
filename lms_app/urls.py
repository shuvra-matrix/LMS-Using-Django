from django.contrib import admin
from django.urls import path
from lms_app import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "base"


urlpatterns = [
    path("",views.index,name='index'),
    path("index/", views.index, name='index'),
    path("create_class/", views.create_class, name='create_class'),
    path("create/",views.create,name='create'),
    path("online_class",views.online,name='online_class'),
    path("create_assignment",views.create_assignment,name='create_assignment'),
    path("view_assignment/",views.view_assignment, name='view_assignment'),
    path("student_view_assignment/", views.student_view_assignment,name='student_view_assignment'),
    path("submit/(?P<assignment_id>\s+)/(?P<teacher_id>\s+)$",views.submit, name='submit'),
    path("view_submission/", views.view_submission, name='view_submission'),
    path("make_submission/",views.make_submission,name='make_submission'),
    path("login/",views.login,name='login'),
    path("logout/",views.logout,name='logout'),
    path("add_course/", views.add_course, name='add_course'),
    path('add_department/', views.add_department, name='add_department'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('view_details/', views.view_details, name='view_details'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),
    path('view_teacher/',views.view_teacher,name='view_teacher'),
    path('assign_class/', views.assign_class, name='assign_class'),
    path('view_assign_class/', views.view_assign_class, name='view_assign_class'),
    path('add_student/', views.add_student, name='add_student'),
    path('view_student',views.view_student,name='view_student'),
    path("update_assignment/(?P<assignment_id>\s+)/$",
         views.update_assignment, name='update_assignment'),
    path("delete_assignment/(?P<assignment_id>\s+)/$",views.delete_assignment, name='delete_assignment'),

    path("updates_assignment/",
         views.updates_assignment, name='updates_assignment'),
    path("update_teacher/(?p<teacher_id>\s+)/$",
         views.update_teacher, name='update_teacher'),
    path("updates_teacher/",
         views.updates_teacher, name='updates_teacher'),
    path("delete_teacher/(?p<teacher_id>\s+)/$",
         views.delete_teacher, name='delete_teacher'),

    path("update_assign_class/(?p<class_id>\s+)/$",
         views.update_assign_class, name='update_assign_class'),
    path("updates_assign_class/",
         views.updates_assign_class, name='updates_assign_class'),
    path("delete_assign_class/(?p<class_id>\s+)/$",
         views.delete_assign_class, name='delete_assign_class'),

    path("update_student/(?p<student_id>\s+)/$",
         views.update_student, name='update_student'),
    path("updates_student/",
         views.updates_student, name='updates_student'),
    path("delete_student/(?p<student_id>\s+)/$",
         views.delete_student, name='delete_student'),

    path("update_course/(?p<course_id>\s+)/(?p<name>\s+)/$",
         views.update_course, name='update_course'),
    path("updates_course/",
         views.updates_course, name='updates_course'),
    path("delete_course/(?p<course_id>\s+)/(?p<name>\s+)/$",
         views.delete_course, name='delete_course'),
    path("updates_department/",
         views.updates_department, name='updates_department'),
    path("update_subject/",
         views.update_subject, name='update_subject'),
    path("delete_class/(?p<class_id>\s+)/$",
         views.delete_class, name='delete_class'),
    path('upload_materials/', views.upload_materials,name='upload_materials'),
    path('view_materials/', views.view_materials, name='view_materials'),
    path("update_materials/(?p<mate_id>\s+)/$",
         views.update_materials, name='update_materials'),
    path("updates_materials/",views.updates_materials, name='updates_materials'),

    path("delete_materials/(?p<mate_id>\s+)/$",
         views.delete_materials, name='delete_materials'),
    path("student_view_materials/", views.student_view_materials,
         name='student_view_materials'),
    
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
