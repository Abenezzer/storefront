from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,  Http404
from django.urls import reverse
from django.db.models import F
from polls.models import Question, Choice


# Create your views here.


def index(request):
    latest_question_list = list(Question.objects.prefetch_related('choice_set').order_by("-pub_date"))
    print(latest_question_list)
    return render(request, "index.html", {"latest_question_list": latest_question_list})

def details(request, question_id):
    question  = Question.objects.get(pk=question_id)
    

    return render(request, "detail.html", {"question": question})
    

def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, "results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk = request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/details.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes= F("votes") + 1
        selected_choice.save()

    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    
                                