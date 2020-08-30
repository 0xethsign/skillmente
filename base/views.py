from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Form1, Form2
from .forms import form1, form2
from django.views.generic import FormView, CreateView


class AddEmail(CreateView):
    model = Form1
    template_name = 'cover.html'
    fields = '__all__'


class AddTutor(CreateView):
    model = Form2
    template_name = 'careers.html'
    fields = '__all__'


class Index(CreateView):
    model = Form1
    template_name = 'cover.html'
    fields = '__all__'
    # success_url = '/'

    # def form_valid(self, form):
    #         # This method is called when valid form data has been POSTed.
    #         # It should return an HttpResponse.
    #     form.send_email()
    #     return super().form_valid(form)
