from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Question, Answer

# Create your views here.


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "account created successfully")
            return redirect("login_view")
        else:
            form.add_error(None, "Correct the errors below")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "logged in")
                return redirect("home")
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login_view")


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(attrs={"rows": 4, "cols": 40}),
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(
                attrs={"rows": 2, "cols": 40, "placeholder": "Provide answer"}
            ),
        }


@login_required
def home_view(request):
    context = {}
    context["user"] = request.user
    context["question_form"] = QuestionForm()
    context["answer_form"] = AnswerForm()
    context["questions"] = Question.objects.exclude(created_by=request.user).order_by(
        "-created_date"
    )
    context["user_questions"] = Question.objects.filter(
        created_by=request.user
    ).order_by("-created_date")
    context["user_answers"] = Answer.objects.filter(created_by=request.user).order_by(
        "-created_date"
    )
    return render(request, "home.html", context)


@login_required
def add_question_view(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user
            question.save()
            messages.success(request, "question added successfully")
            return redirect("home")
    return redirect("home")


@login_required
def user_question_detailed_view(request, question_id):
    context = {}
    question = Question.objects.filter(id=question_id, created_by=request.user)
    if question.exists():
        context["question"] = question.first()
        return render(request, "user_question_detailed.html", context)
    else:
        messages.error(request, "question not found")
        return redirect("home")


@login_required
def question_answer_view(request, question_id):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question_id = question_id
            answer.created_by = request.user
            answer.save()
            messages.success(request, "answer added successfully")
            return redirect("home")
    return redirect("home")


@login_required
def question_answer_like_view(request, q_id, a_id):
    answer = Answer.objects.get(id=a_id)
    answer.likes.add(request.user)
    return redirect("home")
