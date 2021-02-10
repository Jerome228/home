from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Expens
from .forms import ExpensForm

# Create your views here.
def index(request):
    data = {}
    today = timezone.now()
    expMonth = Expens.objects.filter(ddate__year=today.year, ddate__month=today.month)
    family = User.objects.all()
    for user in family:
        if len(user.first_name) > 0:
            nums = [num.amount for num in expMonth if num.person==user]
            data[user.first_name] = sum(nums)
    total = sum(data.values())
    percent = {}
    for key, item in data.items():
        percent[key] = 100 * item / total
    context = {"data": data, "total": total}
    return render(request, "finances/index.html", context)


class ExpensList(ListView):
    model = Expens


class ExpensDetailView(DetailView):

    model = Expens

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ExpensCreate(CreateView):
    model = Expens
    form_class = ExpensForm
    


class ExpensUpdate(UpdateView):
    model = Expens
    form_class = ExpensForm


class ExpensDelete(DeleteView):
    model = Expens
    success_url = reverse_lazy('finances:expenses_list')
