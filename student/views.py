from unicodedata import name
from django.shortcuts import redirect, render
from student.models import Score, Student

def home(request):
    students = Student.objects.order_by('-id')
    return render(request, 'student/home.html', {'students': students})

def create(request):
    if request.method == 'POST':
        student = Student.objects.create(
            name = request.POST['name'],
            nrc = request.POST['nrc'],
            dob = request.POST['dob'],
            phone = request.POST['phone'],
            contact = request.POST['contact'],
        )
        return detail(request, student.id)
    return render(request, 'student/create.html')

def detail(request, student_id):
    student = Student.objects.get(id=student_id)
    score = student.score_set.all()
    return render(request, 'student/detail.html', {'student': student, 'scores': score})

def update(request, student_id):
    if request.method == "POST":
        student = Student.objects.get(id=student_id)
        student.name = request.POST['name']
        student.nrc = request.POST['nrc']
        student.dob = request.POST['dob']
        student.phone = request.POST['phone']
        student.contact = request.POST['contact']
        student.save()
    return detail(request, student_id)

def delete(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('/')

def add_score(request, student_id):
    if request.method == "POST":
        student = Student.objects.get(id=student_id)
        score = Score()
        score.student = student
        score.dltid = request.POST['dltid']
        score.year = request.POST['year']
        score.mark = request.POST['mark']
        score.remark = request.POST['remark']
        score.save()
    return detail(request, student_id)

def delete_score(request, score_id):
    score = Score.objects.get(id=score_id)
    student_id = score.student.id
    score.delete()
    return detail(request, student_id)