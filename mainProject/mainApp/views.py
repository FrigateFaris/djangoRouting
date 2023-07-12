from django.shortcuts import render
from django.http import HttpResponse
from mainApp.models import Comment


# Create your views here.
def home(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')

        Comment.objects.create(comment=comment)

    return render(request, 'index.html')


def about(request):
    comments = Comment.objects.all()
    context = {'comments': comments}
    return render(request, 'index2.html', context=context)