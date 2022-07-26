from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Person , Product
from .forms import PersonForm
from django.views.generic.list import ListView
from django.views.generic import DetailView , View
from django.utils import timezone
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


# TODO: teste do todo

# FIXME : teste fixme

@login_required
def persons_list(request):
    person_search = request.GET.get('searchperson' , None)
    if person_search:
        all_persons = Person.objects.all()
        all_persons = all_persons.filter(first_name__icontains=person_search)
    else:
        all_persons = Person.objects.all()
    return render(request , 'person.html' , {'persons' : all_persons})

@login_required
def person_new(request):
    form = PersonForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request , 'person_form.html' , {'form' : form})

@login_required
def person_update(request , id):
    person = get_object_or_404(Person , pk=id)
    person_context = Person.objects.get(pk=id)
    form = PersonForm(request.POST or None , request.FILES or None , instance=person)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request , 'person_form_update.html' , {'form' : form , 'person' : person_context})

@login_required
def person_delete(request , id):
    person = Person.objects.get(pk=id)
    person.delete()
    return redirect('person_list')

class ListPerson(ListView):
    model = Person

class PersonDetail(DetailView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['product'] = Product.objects.filter(person__id=self.object.id)
        return context

class PersonCreateView(CreateView):
    model = Person
    fields = ['first_name' , 'last_name' , 'age' , 'salary' , 'bio' , 'photo']

class PersonUpdateView(UpdateView):
    model = Person
    fields = ['first_name' , 'last_name' , 'age' , 'salary' , 'bio' , 'photo']

class PersonDeleteView(DeleteView):
    model = Person
    # success_url = reverse_lazy('person_list_cbv')
    def get_success_url(self) -> str:
        return reverse_lazy('person_list_cbv')

class ProductBulk(View):
    def get(self, request):
        products = ['Apple', 'Banana', 'Orange', 'Watermelon']
        list_obj = []
        for product in products:
            list_obj.append(Product(name=product))
        Product.objects.bulk_create(list_obj)
        return HttpResponse('')


