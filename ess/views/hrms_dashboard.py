from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ess.models import Employee, Attendance
from datetime import date

class HRMSDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'hrms_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = date.today()
        
        context['present_employees'] = Attendance.objects.filter(
            date=today, status='Present'
        ).select_related('employee')[:5] 

        context['absent_employees'] = Attendance.objects.filter(
            date=today, status='Absent'
        ).select_related('employee')[:5]

        return context