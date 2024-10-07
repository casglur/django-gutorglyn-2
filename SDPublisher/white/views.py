from django.http import HttpResponse
from django.shortcuts import render_to_response

# Views for Django Templates #
def index(request):
    message = 'hello world'
    
    return render_to_response('index.html', {'message': message})
