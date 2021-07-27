from django.shortcuts import render,redirect
from lms_app.models import Classes,Create_assignment
from django.core.files.storage import FileSystemStorage
# Create your views here.





def index(requests):
    return render(requests,'index.html')



def create_class(requests):
    data=Classes.objects.all().filter(admin_id=1)
    my_dic ={'records':data}
    return render(requests,'createclass.html',context=my_dic)


def create(requests):
    if requests.method == 'POST':
        class_link = requests.POST.get('link')
        department = requests.POST.get('department')
        subject = requests.POST.get('subject')
        date = requests.POST.get('date')
        time = requests.POST.get('time')
        admin_id = 1
        data = Classes.objects.create(admin_id=admin_id,department=department,subject=subject,class_link=class_link,date=date,time=time)
    return render(requests,'createclass.html')



def online(requests):
    data = Classes.objects.all().filter(admin_id=1)
    my_dic = {'records': data}
    return render(requests, 'online_class.html', context=my_dic)


def create_assignment(requests):
    if requests.method == 'POST':
        files = requests.FILES['file']
        file  = FileSystemStorage()
        upload_file = file.save(files.name,files)
        url = file.url(upload_file)
        admin_id=1
        title = requests.POST.get('title')
        des = requests.POST.get('des')
        department = requests.POST.get('department')
        subject = requests.POST.get('subject')
        date = requests.POST.get('date')
        time = requests.POST.get('time')
        data = Create_assignment.objects.create(admin_id=admin_id, title=title, deadline_date=date,deadline_time=time, file=url, despription=des, subject=subject, department=department)
        return render(requests, 'create_assignment.html')
    return render(requests,'create_assignment.html')


def view_assignment(requests):
    data = Create_assignment.objects.all().filter(admin_id=1)
    my_dic = {'records': data}
    return render(requests, 'view_assignment.html', context=my_dic)


def student_view_assignment(requests):
    data = Create_assignment.objects.all().filter(admin_id=1)
    my_dic = {'records': data}
    return render(requests, 'student_view_assignment.html', context=my_dic)
