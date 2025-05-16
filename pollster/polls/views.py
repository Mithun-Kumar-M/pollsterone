from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import question, choice



def index(request):
    latest_question_list = question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)

#Show specifice questions and choices 



def detail(request, question_id):
    try:
        question_obj = question.objects.get(pk=question_id)
    except question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question_obj})


def result(request, question_id):
    question_obj = get_object_or_404(question, pk=question_id)
    total_votes = sum(choice.votes for choice in question_obj.choice_set.all())
    return render(request, 'polls/result.html', {
        'question': question_obj,
        'total_votes': total_votes
    })

def vote(request, question_id):
    question_obj = get_object_or_404(question, pk=question_id)
    try:
        selected_choice = question_obj.choice_set.get(pk=request.POST['choice'])
    except (KeyError, choice.DoesNotExist):
        # Redisplay the question voting form with an error
        return render(request, 'polls/detail.html', {
            'question': question_obj,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # Always return an HttpResponseRedirect after POST to prevent duplicate submissions
        return HttpResponseRedirect(reverse('polls:result', args=(question_obj.id,)))
