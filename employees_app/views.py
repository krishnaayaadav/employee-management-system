from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib import messages
from django.views import View
from django.db.models import Q 

# Create your views here.

# add employee

def homepage(request):
    all_emp = Employee.objects.all()
    return render(request, 'emp_app/home.html', {'all_emp': all_emp})

def not_found_page(request, *args, **kwargs):
    pass

class AddEmployeeView(View):

    def get(self, request):
        form = EmployeeForm()
        return render(request, 'emp_app/add_employee.html', {'form': form})
    
    def post(self, request):
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congrats New Employee Success Created')
            return redirect('homepage') # redirecting at home page

        return render(request, 'emp_app/add_employee.html', {'form': form})

class AupdateEmployee(View):
    def get(self, request,id=None):
            if id is not None and type(id) == int:
                try:
                    emp  = Employee.objects.get(pk=id)
                except Employee.DoesNotExist:
                    return redirect('page_not_found')
                else:
                    form = EmployeeForm(instance=emp)
                    return render(request, 'emp_app/update_employee.html',{'form': form})
            else:
                return redirect('page_not_found')
        
    def post(self, request, id=None):
            if id is not None and type(id) == int:

                try:
                     emp = Employee.objects.get(pk = id)
                except Employee.DoesNotExist:
                     return redirect('page_not_found')
                else:
                    form  = EmployeeForm(request.POST, request.FILES, instance=emp)

                    if form.is_valid():
                         form.save()
                         messages.success(request, 'Employee Data Succeddfuly Update')
                         return redirect('homepage')
                    return render(request, 'emp_app/update_employee.html',{'form': form})
                
            else:
                return redirect('page_not_found')
        
class DeleteEmployee(View):
     def get(self, request, id=None):
            if id is not None and type(id) == int:
                try:
                    emp = Employee.objects.get(pk = id)
                except Employee.DoesNotExist:
                     return redirect('page_not_found')
                else:
                    emp.delete()
                    messages.success(request, 'Employee Successfuly Deleted')
                    return redirect('homepage')
            else:
                return redirect('page_not_found')
            

def search_employees(request,*args, **kwargs):
    all_emp = Employee.objects.all()
    search  = request.GET['search']
    if search is not None:
        employees = Employee.objects.filter(Q(name__icontains = search) |Q(email__icontains = search) | Q(salary__icontains = search) |Q(join_date__icontains = search))

    
    else:
        employees = Employee.objects.all()


        print(f'Search keyword is: {search} Result found are: {employees.count()}  \n {employees}')
    return render(request, 'emp_app/home.html', {'all_emp': employees})
     
        
        


            