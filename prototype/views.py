from django.http import HttpResponse
from pipes import Template
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .forms import *
from django.shortcuts import redirect
# Create your views here.
from .models import *
import pandas as pd
from os import remove


def guardar_datos_csv(arr,pf):
    project = Project.objects.get(id=pf)
    for i in arr:
        if(i[8] == 'null'):
            segment = Segment.objects.get(name='No existe')    
        else:
            segment = Segment.objects.get(name=i[8])
        prototipo = Prototype()
        prototipo.segment_field = segment
        prototipo.project_field = project
        prototipo.name = i[0]
        prototipo.price = i[1]
        prototipo.total_units = i[2]
        prototipo.sold_units = i[3]
        prototipo.m2_terrain = i[4]
        prototipo.m2_constructed = i[5]
        prototipo.m2_habitable = i[6]
        prototipo.floors = i[7]
        prototipo.save()

def handle_uploaded_file(f,pf):  
    with open('static/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)
    valores = pd.read_csv('static/'+f.name)
    valores = valores.fillna("null")
    valores = valores.values.tolist()
    guardar_datos_csv(valores,pf)
    remove('static/'+f.name)

class CreatePrototype(ListView):
    template_name = 'form_prototipo.html'
    model = Segment
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,context={
            'list_segment':Segment.objects.all(),
            'id':self.kwargs['id']
            })
    def post(self,request,*args,**kwargs):
        csv_import = CSV_Form(request.POST, request.FILES)
        project_field = request.POST['project_field']
        if csv_import.is_valid():
                handle_uploaded_file(request.FILES['csv'],project_field)
                return render(request,'prototype_uploaded.html', context={'project_id': project_field})
        else:
            return render(request,self.template_name,context={'Prueba':'No se pudo'})


class PrototypeView(ListView):
    template_name = 'table.html'
    model = Prototype
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,context={
            'list_prototype':Prototype.objects.all(),
            'project_id':self.kwargs['id']
            })

