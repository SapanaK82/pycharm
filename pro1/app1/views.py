from django.shortcuts import render

# Create your views here.
def app1_view(request):
    template_name = 'app1/home.html'
    context = {}
    return render(request, template_name, context)