from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Person
from .forms import PersonForm

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

