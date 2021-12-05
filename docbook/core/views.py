from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.models import Group
from django.contrib import messages
from django.views import View

class HomepageView(TemplateView):
    
    template_name = "index.html"
    
    def get_context_data(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            if self.request.user.groups.exists():
                grp = Group.objects.get(name=self.request.user.groups.get())
                print(type(grp))
                context = super(HomepageView, self).get_context_data(*args, **kwargs)
                context["grp"] = str(grp)
                return context
            else:
                messages.error(self.request, "Group Not Assigned...")




