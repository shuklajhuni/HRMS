from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from ess.models import Employee, Attendance #
from datetime import date

class EmployeeHistoryView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employee_history.html'
    context_object_name = 'employees'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Required for the 'is_marked' check in the template
        context['today'] = date.today() 
        return context

    def post(self, request, *args, **kwargs):
        emp_id = request.POST.get('employee_id')
        new_status = request.POST.get('action')
        
        emp = get_object_or_404(Employee, id=emp_id)
        
        attendance, created = Attendance.objects.update_or_create(
            employee=emp,
            date=date.today(),
            defaults={
                'status': new_status,
                'marked_by': request.user 
            }
        )
        
        messages.success(request, f"Status for {emp.name} saved as {new_status}.")
        return redirect('employee-history')