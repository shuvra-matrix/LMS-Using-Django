from django.shortcuts import render,redirect
from lms_app.models import Classes,Create_assignment,Student,Submit,Teacher,Admin,Course,Department,Subject,Subject_assign,Reading_materials
from django.core.files.storage import FileSystemStorage

# Create your views here.



def index(requests):
    if 'email' in requests.session:
        if 'teacher_id' in requests.session:
            teacher_id = requests.session.get('teacher_id')
            data = Teacher.objects.all().filter(id=teacher_id)
            data2 = Create_assignment.objects.all().filter(admin_id=teacher_id)
            data3 = Submit.objects.all().filter(admin_id=teacher_id)
            data4 = Subject_assign.objects.all().filter(teachers_id=teacher_id)
            total_assignment = len(data2)
            total_submission = len(data3)
            my_dict={
                'teachers': data ,
                'assignment': data2,
                'submit': data3,
                'total_assignment': total_assignment,
                'total_submission': total_submission,
                'class':data4
            }         
            return render(requests,'index.html',context=my_dict)
        if 'student' in requests.session:
            student_id = requests.session.get('student_id')

            data = Student.objects.all().filter(id=student_id)
            name = requests.session.get('s_name')
            department = requests.session['dep']
            data2 = Create_assignment.objects.all().filter(department=department)
            data3 = Submit.objects.all().filter(name=name)
            assignment_no = len(data3)
            submit_no = len(data2)
            message = name
            my_dict = {
                'students':data,
                'assignment': data2,
                'submit':data3,
                'message': message,
                'assignment_no':assignment_no,
                'submit_no': submit_no
            }
            return render(requests, 'index.html',context=my_dict)
        if 'admin' in requests.session:
            return render(requests, 'index.html')
    else:
        return redirect('/login')


def create_class(requests):
    teacher_id=requests.session['teacher_id']
    print(teacher_id)
    data=Classes.objects.all().filter(admin_id=teacher_id)
    sub =Subject_assign.objects.all().filter(teachers_id=teacher_id)
    my_dic ={'records':data,'sub':sub}
    return render(requests,'createclass.html',context=my_dic)


def create(requests):
    if requests.method == 'POST':
        class_link = requests.POST.get('link')
        department = requests.POST.get('department')
        subject = requests.POST.get('subject')
        date = requests.POST.get('date')
        time = requests.POST.get('time')
        admin_id = requests.session['teacher_id']
        data = Classes.objects.create(admin_id=admin_id,department=department,subject=subject,class_link=class_link,date=date,time=time)
        return redirect('/create_class')


def delete_class(requests,class_id):
    print(class_id)
    data = Classes.objects.filter(class_id=class_id).delete()
    return redirect('/create_class')

def online(requests):
    dep = requests.session['dep']
    data = Classes.objects.all().filter(department=dep)
    my_dic = {'records': data}
    return render(requests, 'online_class.html', context=my_dic)


def create_assignment(requests):
    if requests.method == 'POST':
        files = requests.FILES['file']
        file  = FileSystemStorage()
        upload_file = file.save(files.name,files)
        url = file.url(upload_file)
        admin_id = requests.session['teacher_id']
        title = requests.POST.get('title')
        des = requests.POST.get('des')
        department = requests.POST.get('department')
        subject = requests.POST.get('subject')
        date = requests.POST.get('date')
        time = requests.POST.get('time')
        data = Create_assignment.objects.create(admin_id=admin_id, title=title, deadline_date=date,deadline_time=time, file=url, despription=des, subject=subject, department=department)
        return render(requests, 'create_assignment.html')
    teacher_id = requests.session['teacher_id']
    data=Classes.objects.all().filter(admin_id=teacher_id)
    sub =Subject_assign.objects.all().filter(teachers_id=teacher_id)
    my_dic ={'records':data,'sub':sub}
    return render(requests,'create_assignment.html',context=my_dic)


def view_assignment(requests):
    if 'teacher_id' in requests.session:
        id = requests.session['teacher_id']
        data = Create_assignment.objects.all().filter(admin_id=id)
        my_dic = {'records': data}
    return render(requests, 'view_assignment.html', context=my_dic)


def student_view_assignment(requests):
    department = requests.session['dep']
    data = Create_assignment.objects.all().filter(department=department)
    my_dic = {'records': data}
    return render(requests, 'student_view_assignment.html', context=my_dic)


def submit(requests, assignment_id,teacher_id):
    assignment_id = assignment_id
    teacher_id=teacher_id
    student_id = requests.session['student_id']
    return render(requests,'make_submission.html',{'assignment_id':assignment_id,'student_id':student_id,'teacher_id':teacher_id})


def make_submission(requests):
    if requests.method == 'POST':
        student_id = requests.POST.get('student_id')
        assignment_id = requests.POST.get('assignment_id')
        teacher_id = requests.POST.get('teacher_id')
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
            assignment_id=assignment_id, name=name, reg_no=reg_no, roll_no=roll_no, department=departent, file=url,admin_id=teacher_id)
        return redirect('/student_view_assignment')
    return render(requests, 'student_view_assignment.html')




def view_submission(requests):
    if 'teacher_id' in requests.session:
        id = requests.session['teacher_id']
        data = Submit.objects.all().filter(admin_id=id)
        my_dic = {'records': data}
    return render(requests, 'view_submission.html',context=my_dic)

def login(requests):
    if requests.method == 'POST':
        if requests.POST.get('admin') == 'student':
            requests.session['student'] = 'student'
            email = requests.POST.get('email')
            password = requests.POST.get('password')
            data = Student.objects.get(email=email)
            data_pass = data.password
            data_id = data.id
            name = data.name
            requests.session['s_name'] = name 
            requests.session['email'] = email
            requests.session['student_id'] = data_id
            requests.session['dep'] = data.department
            if data_pass == password:
                log_student = requests.session['student']
                message = "hi"
                context = {
                    'messaage': message,
                    'log_student': log_student
                }
                render(requests,'index.html',context=context)
                return redirect('/index')
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
                context = {
                    'messaage': message,
                    'log_teacher': log_teacher,
                }
                render(requests, 'index.html',context=context)
                return redirect('/index')
        elif requests.POST.get('admin') == 'admin':
            email = requests.POST.get('email')
            password = requests.POST.get('password')
            data = Admin.objects.get(email=email)
            data_pass = data.password
            data_id = data.id
            requests.session['email'] = email
            requests.session['admin_id'] = data_id
            requests.session['admin'] = 'admin'
            if data_pass == password:
                message = "hi"
                log_admin = requests.session['admin']
                context = {
                    'messaage': message,
                    'log_admin': log_admin,
                }
                render(requests,'index.html',context=context)
                return redirect('/index')
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


def add_course(requests):
    if requests.method == 'POST':
        course = requests.POST.get('course')
        data = Course.objects.create(course=course)
        return redirect('/add_course')
    courses = Course.objects.all()
    department = Department.objects.all()
    my_dic = {'records': courses, 'department': department}
    return render(requests, 'add_course.html', context=my_dic)


def add_department(requests):
    if requests.method == 'POST':
        department = requests.POST.get('department')
        course = requests.POST.get('course')
        query = Course.objects.get(id=course)
        course_name = query.course
        data = Department.objects.create(course_id=course,course_name=course_name,department=department)
        return redirect('/add_course')
    return render(requests, 'add_course.html')

def add_subject(requests):
    if requests.method == 'POST':
        subject = requests.POST.get('subject')
        department = requests.POST.get('department')
        course = requests.POST.get('course')
        query = Course.objects.get(id=course)
        course_name = query.course
        query = Department.objects.get(id=department)
        department_name = query.department
        data = Subject.objects.create(course_id=course, course_name=course_name, department_name=department_name ,department_id=department, subject=subject)
        return redirect('/add_course')
    return render(requests, 'add_course.html')

def view_details(requests):
    courses = Course.objects.all()
    department = Department.objects.all()
    subject = Subject.objects.all()
    my_dic = {'records': courses, 'department': department,'subject':subject}
    return render(requests, 'view_details.html',context=my_dic)


def add_teacher(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        qualification = requests.POST.get('qualification')
        regno = requests.POST.get('regno')
        address = requests.POST.get('address')
        email = requests.POST.get('email')
        password = requests.POST.get('password')
        data = Teacher.objects.create(name=name,subject=qualification,reg_no=regno,address=address,email=email,password=password)
        return render(requests, 'add_teacher.html')
    return render(requests,'add_teacher.html')


def assign_class(requests):
    if requests.method == 'POST':
        teacher_id = requests.POST.get('teacher')
        data = Teacher.objects.get(id=teacher_id)
        teacher_name = data.name
        teacher_reg_no = data.reg_no
        course = requests.POST.get('course')
        department = requests.POST.get('department')
        subject = requests.POST.get('subject')
        create = Subject_assign.objects.create(course_name=course,department_name=department,subject_name=subject,teachers_id=teacher_id,teachers_name=teacher_name,teachers_reg_no=teacher_reg_no)
        return redirect('/assign_class')

    teachers = Teacher.objects.all()
    course = Course.objects.all()
    department = Department.objects.all()
    subject = Subject.objects.all()
    my_dict = {'teachers':teachers, 'course':course, 'department':department,'subject':subject}
    return render(requests, 'assign_class.html', context=my_dict)



def view_teacher(requests):
    teachers = Teacher.objects.all()
    my_dict = {'teachers':teachers}
    return render(requests,'view_teacher.html',context=my_dict)


def view_assign_class(requests):
    class_assign = Subject_assign.objects.all()
    my_dict={'class_assign':class_assign}
    return render(requests, 'view_assign_class.html',context=my_dict)


def add_student(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        course = requests.POST.get('course')
        department = requests.POST.get('department')
        reg_no = requests.POST.get('reg_no')
        roll_no = requests.POST.get('roll_no')
        year = requests.POST.get('year')
        semester = requests.POST.get('semester')
        address = requests.POST.get('address')
        password = requests.POST.get('password')
        email = requests.POST.get('email')
        data = Student.objects.create(name=name,course=course,department=department,reg_no=reg_no,roll_no=roll_no,year=year,semester=semester,address=address,password=password,email=email)
    return render(requests,'add_student.html')

def view_student(requests):
    student = Student.objects.all()
    my_dict={'student':student}
    return render(requests,'view_student.html',context=my_dict)

def update_assignment(requests,assignment_id):
    teacher_id = requests.session['teacher_id']
    sub =Subject_assign.objects.all().filter(teachers_id=teacher_id)
    data = Create_assignment.objects.all().filter(id=assignment_id)
    my_dic = {'assignment': data,'subject':sub}
    return render(requests,'update_assignment.html',context=my_dic)

def delete_assignment(requests,assignment_id):
    data = Create_assignment.objects.filter(id=assignment_id).delete()
    return redirect('/view_assignment')


def updates_assignment(requests):
    if requests.method == 'POST':
        assignment_id = requests.POST.get('assignment_id')
        data = Create_assignment.objects.get(id=assignment_id)
        url = data.file
        files = requests.FILES['file']
        file = FileSystemStorage()
        upload_file = file.save(files.name, files)
        url = file.url(upload_file)
        admin_id = requests.session['teacher_id']
        title = requests.POST.get('title')
        des = requests.POST.get('des')
        department = requests.POST.get('department')
        subject = requests.POST.get('subject')
        date = requests.POST.get('date')
        time = requests.POST.get('time')
        data = Create_assignment.objects.filter(id=assignment_id).update(admin_id=admin_id, title=title, deadline_date=date,
                                                 deadline_time=time, file=url, despription=des, subject=subject, department=department)
        return redirect('/view_assignment')                                         
    return render(requests, 'view_assignment.html')

def update_teacher(requests,teacher_id):
    data = Teacher.objects.all().filter(id=teacher_id)
    my_dict = {'teacher':data}
    return render(requests,'update_teacher.html',context=my_dict)


def updates_teacher(requests):
    if requests.method == 'POST':
        teacher_id = requests.POST.get('teacher_id')
        name = requests.POST.get('name')
        qualification = requests.POST.get('qualification')
        regno = requests.POST.get('regno')
        address = requests.POST.get('address')
        email = requests.POST.get('email')
        data = Teacher.objects.filter(id=teacher_id).update(name=name, subject=qualification,
                                      reg_no=regno, address=address, email=email)
        return redirect('/view_teacher')


def delete_teacher(requests, teacher_id):
    data = Teacher.objects.filter(id=teacher_id).delete()
    return redirect('/view_teacher')


def update_assign_class(requests,class_id):
    data = Subject_assign.objects.all().filter(id=class_id)
    data2 = Subject.objects.all()
    data3 = Course.objects.all()
    data4 = Department.objects.all()
    data5 = Teacher.objects.all()
    my_dic = {'subject_ass':data,'subject':data2,'department':data4,'course':data3,'teachers':data5}
    return render(requests, 'update_assign_class.html',context=my_dic)


def updates_assign_class(requests):
    if requests.method == 'POST':
        assign_class_id = requests.POST.get('assign_class_id')
        teacher_id = requests.POST.get('teacher')
        data = Teacher.objects.get(id=teacher_id)
        teacher_name = data.name
        teacher_reg_no = data.reg_no
        course = requests.POST.get('course')
        department = requests.POST.get('department')
        subject = requests.POST.get('subject')
        create = Subject_assign.objects.filter(id=assign_class_id).update(course_name=course, department_name=department, subject_name=subject,
                                               teachers_id=teacher_id, teachers_name=teacher_name, teachers_reg_no=teacher_reg_no)
        return redirect('/view_assign_class')


def delete_assign_class(requests,class_id):
    data = Subject_assign.objects.filter(id=class_id).delete()
    return redirect('/view_assign_class')


def update_student(requests,student_id):
    data = Student.objects.all().filter(id=student_id)
    my_dict = {'student':data}
    return render(requests,'update_student.html',context=my_dict)

def delete_student(requests,student_id):
    data = Student.objects.filter(id=student_id).delete()
    return redirect('/view_student')


def updates_student(requests):
    if requests.method == 'POST':
        student_id = requests.POST.get('student_id')
        name = requests.POST.get('name')
        course = requests.POST.get('course')
        department = requests.POST.get('department')
        reg_no = requests.POST.get('reg_no')
        roll_no = requests.POST.get('roll_no')
        year = requests.POST.get('year')
        semester = requests.POST.get('semester')
        address = requests.POST.get('address')
        email = requests.POST.get('email')
        data = Student.objects.filter(id=student_id).update(name=name, course=course, department=department, reg_no=reg_no,
                                      roll_no=roll_no, year=year, semester=semester, address=address,email=email)
        return redirect('/view_student')


def update_course(requests,course_id,name):
    if name == 'course':
        data = Course.objects.all().filter(id=course_id)
        my_dict = {'course':data}
        return render(requests,'update_course.html',context=my_dict)
    elif name == 'department':
        data = Department.objects.all().filter(id=course_id)
        course = Course.objects.all()
        my_dict = {'department':data,'course':course}
        return render(requests,'update_department.html',context=my_dict)
    elif name == 'subject':
        data = Subject.objects.all().filter(id=course_id)
        course = Course.objects.all()
        department = Department.objects.all()
        my_dict = {'subject': data, 'course': course ,'department':department}
        return render(requests, 'update_subject.html', context=my_dict)




def updates_course(requests):
    if requests.method == 'POST':
        course_id = requests.POST.get('course_id')
        course_name = requests.POST.get('course')
        data = Course.objects.filter(id=course_id).update(course=course_name)
        return redirect('/view_details')


def updates_department(requests):
    if requests.method == 'POST':
        dep_id = requests.POST.get('dep_id')
        course = requests.POST.get('course')
        query = Course.objects.get(id=course)
        course_name = query.course
        department = requests.POST.get('department')
        data = Department.objects.filter(id=dep_id).update(course_id=course, course_name=course_name,
                                      department=department)
        return redirect('/view_details')


def update_subject(requests):
    if requests.method == 'POST':
        subject_id = requests.POST.get('sub_id')
        subject = requests.POST.get('subject')
        department = requests.POST.get('department')
        course = requests.POST.get('course')
        query = Course.objects.get(id=course)
        course_name = query.course
        query = Department.objects.get(id=department)
        department_name = query.department
        data = Subject.objects.filter(id=subject_id).update(course_id=course, course_name=course_name,
                                      department_name=department_name, department_id=department, subject=subject)
        return redirect('/view_details')

def delete_course(requests,course_id,name):
    if name == 'course':
        data = Course.objects.filter(id=course_id).delete()
        return redirect('/view_details')
    elif name == 'department':
        data = Department.objects.filter(id=course_id).delete()
        return redirect('/view_details')
    elif name == 'subject':
        data = Subject.objects.filter(id=course_id).delete()
        return redirect('/view_details')


def upload_materials(requests):
    if requests.method == 'POST':
        files = requests.FILES['file']
        file = FileSystemStorage()
        upload_file = file.save(files.name, files)
        url = file.url(upload_file)
        admin_id = requests.session['teacher_id']
        title = requests.POST.get('title')
        des = requests.POST.get('des')
        department = requests.POST.get('department')
        subject = requests.POST.get('subject')
        data = Reading_materials.objects.create(admin_id=admin_id, title=title,
                                                 file=url, despription=des, subject=subject, department=department)
        return render(requests, 'upload_materials.html')

    teacher_id = requests.session['teacher_id']
    data = Classes.objects.all().filter(admin_id=teacher_id)
    sub = Subject_assign.objects.all().filter(teachers_id=teacher_id)
    my_dic = {'records': data, 'sub': sub}
    return render(requests,'upload_materials.html',context=my_dic)


def view_materials(requests):
    if 'teacher_id' in requests.session:
        id = requests.session['teacher_id']
        data = Reading_materials.objects.all().filter(admin_id=id)
        my_dic = {'records': data}
        return render(requests,'view_materials.html',context=my_dic)


def update_materials(requests,mate_id):
    teacher_id = requests.session['teacher_id']
    sub = Subject_assign.objects.all().filter(teachers_id=teacher_id)
    data = Reading_materials.objects.all().filter(id=mate_id)
    my_dic = {'assignment': data, 'subject': sub}
    return render(requests, 'update_materials.html',context=my_dic)



def updates_materials(requests):
    if requests.method == 'POST':
        mate_id = requests.POST.get('mate_id')
        data = Reading_materials.objects.get(id=mate_id)
        url = data.file
        files = requests.FILES['file']
        file = FileSystemStorage()
        upload_file = file.save(files.name, files)
        url = file.url(upload_file)
        admin_id = requests.session['teacher_id']
        title = requests.POST.get('title')
        des = requests.POST.get('des')
        department = requests.POST.get('department')
        subject = requests.POST.get('subject')
        data = Reading_materials.objects.filter(id=mate_id).update(admin_id=admin_id, title=title, 
                                                                         file=url, despription=des, subject=subject, department=department)
        return redirect('/view_materials')



def delete_materials(requests,mate_id):
    data = Reading_materials.objects.filter(id=mate_id).delete()
    return redirect('/view_materials')


def student_view_materials(requests):
    dep = requests.session['dep']
    data = Reading_materials.objects.all().filter(department=dep)
    my_dic = {'data':data}
    return render(requests,'student_view_materials.html',context=my_dic)



 
