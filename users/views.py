from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView, View

from .forms import UserRegForm, UserUpdate, ProfileImg
from movies.views import GenreYear
from movies.models import Movie


class Registration(CreateView, GenreYear):

    def post(self, request):
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Пользователь {username} был успешно создан")
            return redirect("log")

    def get(self,  request):
        form = UserRegForm()
        view = {"form": form, "title": "Регистрация пользователя"}
        return render(request, "users/registration.html", view)


class Profile(LoginRequiredMixin, View):

    def post(self, request):
        img_prolile = ProfileImg(
            request.POST, request.FILES, instance=request.user.profile
        )
        update_user = UserUpdate(request.POST, instance=request.user)
        if update_user.is_valid() and img_prolile.is_valid():
            update_user.save()
            img_prolile.save()
            messages.success(request, f"Ваш аккаунт был обновлен")
            return redirect('profile')

    def get(self,  request):
        img_prolile = ProfileImg(instance=request.user.profile)
        update_user = UserUpdate(instance=request.user)
        view = {"img_prolile": img_prolile, "update_user": update_user}

        return render(request, "users/profile.html", view)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["year"] = Movie.objects.filter(draft=False).values("year")
        return context



