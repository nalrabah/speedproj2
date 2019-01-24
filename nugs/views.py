from django.shortcuts import render
# Create your views here.
def message(request):
    return render(request, 'message.html', {'msg':'Hello World! I like nugs'})