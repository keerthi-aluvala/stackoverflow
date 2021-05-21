from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import Question, Answer, Comment
from django.core.paginator import Paginator
from .forms import AnswerForm
from django.contrib import messages

def home(request):
    if 'q' in request.GET:
        q=request.GET['q']
        quests=Question.objects.filter(title_icontains=q).order_by('-id')
    else:
        quests = Question.objects.all().order_by('-id')   
    paginator=Paginator(quests,1)
    page_num = request.GET.get('page',1)
    quests=paginator.page(page_num)
    return render(request,'home.html',{'quests':quests})


def detail(request,id):
    quest=Question.objects.get(pk=id)
    tags=quest.tags.split(',')
    answers=Answer.objects.filter(question=quest)
    answerform=AnswerForm
    if request.method=='POST':
        answerData=AnswerForm(request.POST)
        if answerData.is_valid:
            answer=answerData.save(commit=False)
            answer.question=quest
            answer.user=request.user
            answer.save()
            messages.success(request,'Answer has been submitted!')
    return render(request,'detail.html',{
        'quest':quest,
        'tags':tags,
        'answers':answers,
        'answerform':answerform,
    })


def save_comment(request):
    if request.method=='POST':
        comment=request.POST['comment']
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        Comment.objects.create(
            answer=answer,
            comment=comment,
            user=user
        )
        return JsonResponse({'bool':True})

def save_upvote(request):
    if request.method=='POST':
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        check=UpVote.objects.filter(answer=answer,user=user).count()
        if check > 0:
            return JsonResponse({'bool':False})
        else:
            UpVote.objects.create(
                answer=answer,
                user=user
            )
        return JsonResponse({'bool':True})