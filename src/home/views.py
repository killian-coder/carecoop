
from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name = "index.html"

# -*- coding: utf-8 -*-
from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name="home/index.html"

