from django.shortcuts import render
from .forms import MpesaForm
from .utils import stk_push


def home(request):
    if request.method =="POST":
        form = MpesaForm(request.POST)
        if form.is_valid():
            tel = form.cleaned_data['phone_number']
            amount = form.cleaned_data['amount']
            stk_push(tel, amount, 'something', 'something else')
    else:
        form = MpesaForm()
    context = {'form':MpesaForm()}
    return render(request, 'index.html', context)