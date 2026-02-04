from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q
from ess.models import Employee, Attendance
from datetime import date

class HRAnalyticsView(LoginRequiredMixin, TemplateView):
    template_name = 'hr_analytics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Capture filter inputs from the URL
        f_date = self.request.GET.get('date', date.today().isoformat())
        f_unit = self.request.GET.get('unit', '')

        emp_qs = Employee.objects.all()
        att_qs = Attendance.objects.filter(date=f_date)

        if f_unit:
            emp_qs = emp_qs.filter(department=f_unit)
            att_qs = att_qs.filter(employee__department=f_unit)

        # Total Employee Stats
        context['gender_stats'] = emp_qs.aggregate(
            male_staff=Count('id', filter=Q(gender='Male', department='Staff')),
            female_staff=Count('id', filter=Q(gender='Female', department='Staff')),
            male_workers=Count('id', filter=Q(gender='Male', department='Workers')),
            female_workers=Count('id', filter=Q(gender='Female', department='Workers')),
            total_employees=Count('id')
        )

        # Attendance Stats
        context['attendance_stats'] = att_qs.filter(status='Present').aggregate(
            male_present=Count('id', filter=Q(employee__gender='Male')),
            female_present=Count('id', filter=Q(employee__gender='Female')),
            total_present=Count('id')
        )

        context['selected_date'] = f_date
        context['selected_unit'] = f_unit
        return context