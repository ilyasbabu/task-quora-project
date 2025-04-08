"""
URL configuration for project_quora project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from core.views import (
    signup_view,
    login_view,
    home_view,
    logout_view,
    add_question_view,
    question_detailed_view,
    question_answer_view,
    question_answer_like_view,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", signup_view, name="signup_view"),
    path("login/", login_view, name="login_view"),
    path("logout/", logout_view, name="logout_view"),
    path("", home_view, name="home"),
    path("question/add/", add_question_view, name="add_question_view"),
    path(
        "question/<int:question_id>",
        question_detailed_view,
        name="question_detailed_view",
    ),
    path(
        "question/answer/<int:question_id>",
        question_answer_view,
        name="question_answer_view",
    ),
    path(
        "question/<int:q_id>/answer/<int:a_id>/like",
        question_answer_like_view,
        name="question_answer_like_view",
    ),
]
