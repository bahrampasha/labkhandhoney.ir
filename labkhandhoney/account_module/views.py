from django.shortcuts import render
from django.views import View

from account_module.forms import RegisterForm


# Create your views here.
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {'register_form': register_form}
        return render(request, 'register.html', context)

    def post(self, request):
        pass
