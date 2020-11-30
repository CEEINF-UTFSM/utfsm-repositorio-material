from django.shortcuts import render
from ramos.models import Ramo
# Create your views here.


def home(request):
	all_ramos = Ramo.objects.all()
	ramo_by_semestre = {}
	for ramo in all_ramos:
		semestre = str(ramo.semestre)
		if semestre not in ramo_by_semestre.keys():
			ramo_by_semestre[semestre] = []
		ramo_by_semestre[semestre].append(ramo.sigla)
	ramo_by_semestre = list(ramo_by_semestre.items())
	ramo_by_semestre.sort()
	context = {
		'ramos':all_ramos,
		'ramo_by_semestre':ramo_by_semestre
	}
	print(context)
	return render(request, "home.html", context)
