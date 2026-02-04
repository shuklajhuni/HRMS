from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from ess.models import Employee 

#CRUD Views for Employee Profile Management
class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employee_profile_form.html'
    fields = ['emp_code', 'name', 'gender', 'department', 'official_email', 'profile_photo']
    success_url = reverse_lazy('employee-manage') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetching all records for the history table below the form
        context['employees'] = Employee.objects.all().order_by('-id')
        return context

    def form_valid(self, form):
        emp_code = form.cleaned_data.get('emp_code')
        email = form.cleaned_data.get('official_email')
        
        if not str(emp_code).isdigit():
            form.add_error('emp_code', "Employee Code must contain only numbers.")
            return self.form_invalid(form)

        if '@' not in email:
            form.add_error('official_email', "Official Email must include the @ symbol.")
            return self.form_invalid(form)

        messages.success(self.request, "Employee record created successfully!")
        return super().form_valid(form)

class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employee_profile_form.html'
    fields = ['emp_code', 'name', 'gender', 'department', 'official_email', 'profile_photo']
    success_url = reverse_lazy('employee-manage')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Keep the history table visible while editing
        context['employees'] = Employee.objects.all().order_by('-id')
        return context

    def form_valid(self, form):
        messages.success(self.request, "Employee record updated successfully!")
        return super().form_valid(form)

class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee-manage')
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, "Employee record deleted.")
        return super().delete(request, *args, **kwargs)