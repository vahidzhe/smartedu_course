from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from courses.models import Course
from . forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

# def index(request):
#     return render(request,'index.html')

class IndexView(TemplateView):
    
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available=True).order_by('-date')[:2]
        context['total_courses'] = Course.objects.filter(available=True).count()

        return context




# def about(request):
#     return render(request,'about.html')

class AboutView(TemplateView):
    
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available=True).order_by('-date')[:2]
        context['total_courses'] = Course.objects.filter(available=True).count()

        return context

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    
    
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
        
    success_messages = 'Ugurla gonderildi'
    