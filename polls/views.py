from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("You are seeing all questions with thair choice")

def details(request, question_id):
    return HttpResponse(f"You are seeing a detail for question_id {question_id}")
    

def results(request, question_id):
    return HttpResponse(f"you are seeing a result for question id {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You are voting for question_id {question_id}")
