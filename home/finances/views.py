from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Expens, Salary
from .forms import ExpensForm, SalaryForm


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
        try:
            percent[key] = 100 * item / total
        except ZeroDivisionError:
            percent[key] = 0.0
    context = {"data": data, "total": total, "percentages": percent}
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

def expensChart(request):
    wages = [2700, 1200]
    data = {}
    today = timezone.now()
    querySet = Expens.objects.filter(ddate__year=today.year, ddate__month=today.month)
    family = User.objects.all()
    for user in family:
        if len(user.first_name) > 0:
            nums = [num.amount for num in querySet if num.person==user]
            data[user.first_name] = sum(nums)
    total = sum(data.values())
    labels = []
    percents = []
    amount = []
    for key, item in data.items():
        labels.append(key)
        try:
            percent = 100 * item / total
        except ZeroDivisionError:
            percent = 0.0
        percents.append(percent)
        amount.append(item)
    wpercents = [item/sum(wages) for item in wages]
    toPay = [item*total for item in wpercents]
    return JsonResponse(data={
        'labels': labels,
        'data': percents,
        'amount': amount,
        'wages': wages,
        'topay': toPay,
    })

class SalaryList(ListView):
    model = Salary


class SalaryDetailView(DetailView):

    model = Salary

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class SalaryCreate(CreateView):
    model = Salary
    form_class = SalaryForm


class SalaryUpdate(UpdateView):
    model = Salary
    form_class = SalaryForm


class SalaryDelete(DeleteView):
    model = Salary
    success_url = reverse_lazy('finances:salary_list')