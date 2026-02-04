from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class SelectionDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard_select.html'
    login_url = '/login/'