from django.shortcuts import render
from .models import Chambre,Catalogue,Testimonial,Reserved
import datetime
from .forms import ReservationForm
# Create your views here.

def index (request):
    chambres= Chambre.objects.all()
    catalogues= Catalogue.objects.all()
    testimonials = Testimonial.objects.all()
    reserved= Reserved.objects.all()
    if request.method == 'POST':
        checki = request.POST.get('check_in')
        checko = request.POST.get('check_out')


        # l = check.split()
        print(checki,checko)
        # print("-".join(l))
        # checking = Activity.objects.filter(check_in=f'{l[2]}{l[1]}{l[0]}')
        checking = Reserved.objects.filter(check_in__gte=datetime.datetime.utcnow(), check_in=checki,check_out=checko)

        return render(request,"index.html",{'chambres': chambres,'testimonial': testimonials,
    'catalogues': catalogues,'reserved': reserved,'checking':checking})

    return render(request,"index.html",{'chambres': chambres,'testimonial': testimonials,
    'catalogues': catalogues,'reserved': reserved})
def reservation (request):
   
    if request.method == 'POST':
        form = ReservationForm(request.POST or None)
        if form.is_valid():
            form.save()
            print("YES")
    else:
        form = ReservationForm()
        print("WRONG")
    return render(request, "reservation.html",{'form': form})
def contact(request):
    return  render (request, "contact.html")
def blog (request):
    chambres = Chambre.objects.all()
    return render (request, "blog.html",{'chambres': chambres})
def about(request):
    return render (request, 'about.html')