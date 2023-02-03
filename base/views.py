from django.shortcuts import render

from backend.handlers.answers_handler import assess_answer


# Create your views here.


def home(request):
    text = request.POST.get('text')
    quest = "What is Internet?"
    print(text)
    # text = 'sajeel'

    if request.method == 'POST':
        res = assess_answer(1, text, 'GxU8XjEKA2SIrK1IB1b8eJPflDRLXVNBTIlblupP')

        context = {'res': f"Answer quality is \"{res}\"", 'text': text, 'quest': quest}
        return render(request, 'base/home.html', context)
    context = {}
    return render(request, 'base/home.html', context)


def about(request):
    context = {}
    return render(request, 'base/about.html', context)
