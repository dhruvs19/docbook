from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.models import Group
from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, render
from django.db.models import Count
import numpy as np
import matplotlib.pyplot as plt1
from doctor.models import *
import matplotlib
matplotlib.use('Agg')

class HomepageView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Location.objects.all()
        context['specializations'] = Specialization.objects.all()
        context["doctorGrpah"] =  HomepageView.doctorSpecializationLocation()
        return context
    
    @classmethod
    def doctorSpecializationLocation(cls):
        docres = DocProfile.objects.values('specialization').order_by('specialization').annotate(count=Count('specialization'))
        spec_count = []
        doc_list = []
        for i, d in enumerate(docres):
            doc_list.append(d['count'])
            spec_count.append(d['specialization'])
    
        labels = np.array(spec_count)
        sizes = np.array(doc_list)
        explode = (0, 0, 0, 0) 
        plt1.clf()
        plt1.pie(sizes, explode=explode, labels=labels,shadow=True, startangle=90, autopct='%1.1f%%')
        plt1.title("Doctors Distribution")
        docfilename = 'media/doctors/specialization_graph/' + 'doctorspecialization' + '.png'
        plt1.savefig(docfilename)


class AboutPage(TemplateView):
    template_name = "about.html"

class ContactPage(TemplateView):
    template_name = "contact.html"