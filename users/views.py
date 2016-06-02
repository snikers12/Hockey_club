import json

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import serializers
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView, UpdateView

from users.forms import UserProfileForm
from users.models import UserProfile


def login(request):
    if request.user.is_authenticated():
        return redirect(reverse("news:news"))

    if request.method == "GET":
        context = {}
        if "next" in request.GET:
            context["next"] = "?next=" + request.GET["next"]
        return render(request, "users/login.html", context)

    elif request.method == "POST":
        user = authenticate(
                username=request.POST["username"],
                password=request.POST["password"]
        )
        if user is not None:
            auth_login(request, user)
            if "next" in request.GET:
                return redirect(request.GET["next"])
            else:
                return redirect(reverse("news:news"))
        else:
            return redirect(reverse("users:login"))
    else:
        return HttpResponse("405")


def logout(request):
    auth_logout(request)
    return redirect(reverse("news:news"))


class UserProfileFormView(UpdateView):
    model = UserProfile
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:edit_profile')
    form_class = UserProfileForm

    @login_required(login_url=reverse_lazy("users:login"))
    def get_object(self, queryset=None):
        return self.model.objects.get_or_create(user=self.request.user)[0]

    @login_required(login_url=reverse_lazy("users:login"))
    def get_context_data(self, **kwargs):
        context = super(UserProfileFormView, self).get_context_data(**kwargs)
        return context


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = "users/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)