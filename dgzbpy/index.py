from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html', {'title': 'this is my front page title', 'message': 'this is my front page'})
