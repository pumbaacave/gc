from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.template import loader
from django.views import generic
from django.utils import timezone
from . import getData


class TopPageView(generic.View):
    template_name = 'showroom/toppage.html'
    context_object_name = 'targetDict'
    def get(self, request, *args, **kwargs):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        data = getData.run()
        targetDict = getData.getOneRecord(data)
        context = {'targetDict': targetDict}
        return render(request, 'showroom/toppage.html', context)