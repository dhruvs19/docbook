from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.models import Group
from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, render
from django.db.models import Count
import matplotlib.ticker as ticker
import base64
import numpy as np
import matplotlib.pyplot as plt1
from doctor.models import *
from io import BytesIO
import matplotlib
matplotlib.use('Agg')

class HomepageView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Location.objects.all()
        context['specializations'] = Specialization.objects.all()
        context["doctorGrpah"] =  doctorSpecializationLocation()
        return context
    
def doctorSpecializationLocation():
    docres = DocProfile.objects.values('specialization').order_by('specialization').annotate(count=Count('specialization'))
    spec_count = []
    doc_list = []
    print(docres)
    for i, d in enumerate(docres):
        doc_list.append(d['count'])
        spec_count.append(d['specialization'])
  
    labels = np.array(spec_count)
    sizes = np.array(doc_list)
    explode = (0, 0, 0, 0) 
    
    print(labels)
    print(sizes)

    # plt1.locator_params(axis="y", integer=True, tight=True)
   
    plt1.pie(sizes, explode=explode, labels=labels,autopct='%1.1f%%',shadow=True, startangle=90)
    
    # plt1.xlabel("specialization")
    # plt1.ylabel("Number of Doctors")
    plt1.title("Specialization vs Doctors")
  
    docbuffer = BytesIO()
    docfilename = 'media/doctors/specialization_graph/' + 'doctorspecialization' + '.png'
    plt1.savefig(docfilename)
    docb64 = base64.b64encode(docbuffer.getvalue()).decode()
    docbuffer.close()
    return docb64


class AboutPage(TemplateView):
    template_name = "about.html"

class ContactPage(TemplateView):
    template_name = "contact.html"