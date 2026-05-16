from django.shortcuts import render
from .models import Employee

def employee_list(request):
    employees = Employee.objects.prefetch_related('work_images').all()
    
    employee_data = []
    for emp in employees:
        experiences = [line.strip() for line in emp.experience.split('\n') if line.strip()]
        works = [line.strip() for line in emp.work_done.split('\n') if line.strip()]
        
        employee_data.append({
            'employee': emp,
            'experiences': experiences,
            'works': works,
        })
        
    return render(request, 'team/employee_list.html', {'employee_data': employee_data})
