from django import forms 
from .models import Employee


class EmployeeForm(forms.ModelForm):
    name = forms.CharField(required= True, error_messages={'required': 'Name is required', 'placeholder': 'Enter name here'})

    def clean_name(self):
        name = self.cleaned_data['name']

        if (len(name) <7):
                raise forms.ValidationError('Name must contains as least 7 characters!')
            
        if (str(name).isalpha() == False):
            raise forms.ValidationError('Name does not contains numbers or special sysmbols')
        return name

    # def clean(self):
    #     cleaned_data = super().clean()

    #     if('name' in cleaned_data.keys()):
    #         name = cleaned_data['name']

    #         if (len(name) <7):
    #             raise forms.ValidationError('Name must contains as least 7 characters!')
            
    #         if (str(name).isalpha() == False):
    #             raise forms.ValidationError('Name does not contains numbers or special sysmbols')
    #         return name
        
        # if ('email' in  cleaned_data.keys()):
        #     email = cleaned_data['email']

        #     if (len(email) < 11):
        #         raise forms.ValidationError('Email must contains 11 charaters')
        #     return email
            
        # if ('salary' in cleaned_data.keys()):
        #     salary = cleaned_data['salary']
        #     if(salary <= 10000):
        #         raise forms.ValidationError('Salary must be greater than 10000')
            
        #     return salary
    
   

        
            
    class Meta:
        model  = Employee
        fields = ('name', 'email', 'dept', 'salary', 'image')


        error_messages = {
            'image': {'required': 'Image is required'},
            'name': {'required': 'Name is required'},
            'email': {'required': 'Email is required'},
            'salary': {'required': 'Salary is required'},
            'dept': {'required': 'Department is required'}
        }

       