from __future__ import absolute_import

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from django.db.models import Q

from .forms import RequestForm
from .models import Car, Request
from .tasks import get_car_data

from django_datatables_view.base_datatable_view import BaseDatatableView

from eztables.views import DatatablesView
from django.template import add_to_builtins

add_to_builtins('eztables.templatetags.eztables')
add_to_builtins('djangojs.templatetags.js')

@login_required()
def index(request):
    return render(request, 'com_local/homepage.html', {'form': RequestForm()})


@login_required()
def new_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.user = request.user
            req.save()
            form.save_m2m()

            #req.get_requested_cars()
            _run_cars_data_update_tasks(req)

            return HttpResponseRedirect(reverse('com_local:request_cars', kwargs={'pk': req.id}))
    else:
        form = RequestForm()

    return render(request, 'com_local/request_new.html', {'form': form})


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class RequestCarsList(LoginRequiredMixin, SingleObjectMixin, ListView):
    template_name = 'com_local/request_cars.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Request.objects.all())
        return super(RequestCarsList, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.car_set.all()

    def get_context_data(self, **kwargs):
        context = super(RequestCarsList, self).get_context_data(**kwargs)
        context['request_obj'] = self.object
        return context


class RequestsView(LoginRequiredMixin, DatatablesView):
    model = Request
    fields = {
        'code': 'code',
        #'absolute_url': 'absolute_url',
        'created': 'created',
        'updated': 'updated',
    }

    def json_response(self, data):
        return HttpResponse(
            JsonResponse(data)
        )


class RequestsViewJson(LoginRequiredMixin, BaseDatatableView):

    model = Request
    columns = ['code', 'created', 'updated']
    order_columns = ['code', 'created', 'updated']

    max_display_length = 500

    def filter_queryset(self, qs):
            # use parameters passed in POST request to filter queryset

            # simple example:
            search = self.request.POST.get('search[value]', None)
            print 'search', search
            if search:
                qs = qs.filter(code__istartswith=search)

            return qs


def _run_cars_data_update_tasks(req):
    reg_numbers = req.requested_reg_numbers.all()
    print reg_numbers

    if not len(reg_numbers):
        return None

    for nr in reg_numbers:
        new_car = Car()
        new_car.request = req
        new_car.car_reg = nr.name
        req.car_set.add(new_car)
        get_car_data.apply_async(args=(new_car,))