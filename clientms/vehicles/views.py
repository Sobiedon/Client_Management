from django.contrib.auth.mixins import LoginRequiredMixin  # New
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import Vehicle
from django.urls import reverse_lazy


class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'


class VehicleDetailView(LoginRequiredMixin, DetailView):
    model = Vehicle
    template_name = 'vehicle_detail.html'
    login_url = 'login'


class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    fields = ('customer_name', 'vehicle_make', 'model', 'VIN_number', 'notes')
    template_name = 'vehicle_edit.html'
    success_url = reverse_lazy('vehicle_list')


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehicle
    template_name = 'vehicle_delete.html'
    success_url = reverse_lazy('vehicle_list')


class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    template_name = 'vehicle_new.html'
    fields = ('customer_name', 'vehicle_make', 'model', 'VIN_number', 'date_of_purchase', 'date_of_last_Service',
              'notes')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
