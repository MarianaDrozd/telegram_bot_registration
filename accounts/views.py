from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import TemplateView, View, RedirectView, DetailView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from accounts.models import Account, User
import json
import logging

logger = logging.getLogger()


# Create your views here.
class HomeView(TemplateView):
    """A view for the homepage."""
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['account'] = Account.objects.filter(user=self.request.user).first()
        else:
            context['account'] = None
        context['user'] = self.request.user
        return context


class RegisterView(View):
    """A view for registering"""

    def post(self, request):
        return redirect('https://t.me/django_telegram_registration_bot')


class AccountView(DetailView):
    model = Account
    context_object_name = 'account'
    pk_url_kwarg = 'pk'
    template_name = 'account.html'


@csrf_exempt
def save_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            logger.info(data)
            username = data.get('username')
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            password = data.get('password')
            telegram_id = data.get('telegram_id')
            photo = data.get('photo')
            user = User.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=make_password(password),
            )
            user.save()
            new_account = Account.objects.create(
                user=user,
                photo_url=photo,
                telegram_id=telegram_id,
            )
            new_account.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'failed', 'error': str(e)})
