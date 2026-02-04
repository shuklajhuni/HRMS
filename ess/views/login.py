from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class JSCodeLoginView(LoginView):
    """Customized Login View with Redirect for Authenticated Users"""
    template_name = 'login.html' 
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('selection-dashboard')