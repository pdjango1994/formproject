from django.shortcuts import render
from testapp.forms import BeerForm
# Create your views here.
def BeerView(request):
    form = BeerForm()# creating form object and transfer that object to the template file
    if request.method=='POST':
        form =BeerForm(request.POST)
        if form.is_valid():
            print('Beer is added succufully...')
            print('Name  of beer :' , form.cleaned_data['name'])
            print('Price of beer :' , form.cleaned_data['price'])
            return render(request,'testapp/thanks.html')

    return render(request,'testapp/beer.html',{'form':form})
