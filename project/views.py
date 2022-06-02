from django.shortcuts import render

from project.forms import TableForm


def table(request):
    form = TableForm()
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'table.html', context)




