from django.shortcuts import render

from.models import Question
# Create your views here.
def home(request):
    question = Question.objects.all()
    return render(
        request,
        'poll/home.html',
        {
            "questions": question
        })


def vote(request, q_id):
    q = Question.objects.get(pk=q_id)
    return render(request, 'poll/vote.html',{
        "question": q
    })

def result(request, q_id):
    pass