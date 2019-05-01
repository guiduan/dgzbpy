from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html', {'title': 'this a title', 'message': 'this is a message'})
