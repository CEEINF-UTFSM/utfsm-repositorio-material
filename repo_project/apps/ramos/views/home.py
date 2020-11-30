from django.shortcuts import render
from ramos.models import Ramo
# Create your views here.


def home(request):
	all_ramos = Ramo.objects.all()
	context = {
		'ramos': all_ramos
	}
	print(context)
	return render(request, "home.html", context)
