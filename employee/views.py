from django.shortcuts import render
from django .views .generic import TemplateView

# Create your views here.


class HomeView(TemplateView):
    template_name = "index.html"
#    def get(self,request):
        #return render(self.request, 'index.html')
