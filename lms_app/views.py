from django.shortcuts import render,redirect
from lms_app.models import Classes,Create_assignment,Student,Submit,Teacher
from django.core.files.storage import FileSystemStorage

# Create your views here.





def index(requests):
    if 'email' in requests.session:
        return render(requests,'index.html')
    else:
        return render(requests,'login.html')



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
    log_teacher = requests.session['teacher']
    print(log_teacher)
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
    department = requests.session['dep']
    data = Create_assignment.objects.all().filter(department=department)
    my_dic = {'records': data}
    return render(requests, 'view_assignment.html', context=my_dic)


def student_view_assignment(requests):
    department = requests.session['dep']
    data = Create_assignment.objects.all().filter(department=department)
    my_dic = {'records': data}
    return render(requests, 'student_view_assignment.html', context=my_dic)


def submit(requests, assignment_id):
    assignment_id = assignment_id
    student_id = requests.session['student_id']
    return render(requests,'make_submission.html',{'assignment_id':assignment_id,'student_id':student_id})


def make_submission(requests):
    if requests.method == 'POST':
        student_id = requests.POST.get('student_id')
        assignment_id = requests.POST.get('assignment_id')
        data = Student.objects.get(id=student_id)
        name = data.name
        departent = data.department
        reg_no = data.reg_no
        roll_no = data.roll_no
        files = requests.FILES['file']
        file = FileSystemStorage()
        upload_file = file.save(files.name, files)
        url = file.url(upload_file)
        data = Submit.objects.create(
            assignment_id=assignment_id, name=name, reg_no=reg_no, roll_no=roll_no, department=departent, file=url)
        return render(requests, 'student_view_assignment.html')
    return render(requests, 'submit.html')




def view_submission(requests):
    department = requests.session['dep']
    data = Submit.objects.all().filter(department=department)
    my_dic = {'records': data}
    return render(requests, 'view_submission.html',context=my_dic)

def login(requests):
    if requests.method == 'POST':
        if requests.POST.get('admin') == 'student':
            email = requests.POST.get('email')
            password = requests.POST.get('password')
            data = Student.objects.get(email=email)
            data_pass = data.password
            data_id = data.id
            requests.session['email'] = email
            requests.session['student_id'] = data_id
            requests.session['dep'] = data.department
            requests.session['student'] = 'student'
            if data_pass == password:
                log_student = requests.session['student']
                message = "hi"
                context = {
                    'messaage': message,
                    'log_student': log_student
                }
                return render(requests,'index.html',context=context)
        elif requests.POST.get('admin') == 'teacher':
            email = requests.POST.get('email')
            password = requests.POST.get('password')
            data = Teacher.objects.get(email=email)
            data_pass = data.password
            data_id = data.id
            requests.session['email'] = email
            requests.session['teacher_id'] = data_id
            requests.session['teacher'] = 'teacher'
            if data_pass == password:
                message = "hi"
                log_teacher = requests.session['teacher']
                print(log_teacher)
                context = {
                    'messaage': message,
                    'log_teacher': log_teacher,
                }
                return render(requests, 'index.html',context=context)
        elif requests.POST.get('admin') == 'admin':
            return render(requests, 'index.html')
    return render(requests,'login.html')

def logout(requests):
    if requests.session.has_key('email'):
        try:
            for key in list(requests.session.keys()):
                del requests.session[key]
            return render(requests,'login.html')
        except:
            pass
    else:
        return render(requests, 'login.html')
