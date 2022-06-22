from django.shortcuts import render

from project.forms import TableForm, TableForms


def table(request):
    form = TableForm()
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'table.html', context)

def index(request):
    form = TableForms()
    if request.method == 'POST':
        form = TableForms(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'index.html', context)





