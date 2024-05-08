# views.py
from django.shortcuts import render, redirect
from .models import TestForm
from .forms import TestFormForm
import json

def form_view(request):
    if request.method == 'POST':
        form = TestFormForm(request.POST)
        if form.is_valid():
            test_form = form.save(commit=False)
            test_form.data = json.loads(request.POST.get('data'))
            test_form.save()
            return redirect('form_view')
    else:
        form = TestFormForm()
        data = [["" for _ in range(30)] for _ in range(10)]
    return render(request, 'errortrackingformapp/form.html', {'form': form, 'data': data})


# dat = TestForm.objects.all()

# for dt in dat:
#     column_counts = [0] * len(dt.data[0]) 
#     for row in dt.data:
#         for index, value in enumerate(row):
#             if value == 'X':
#                 column_counts[index] += 1

#     # Sort the counts in ascending order
#     sorted_counts = column_counts
#     print("Counts of 'X's in each column in ascending order:", sorted_counts)