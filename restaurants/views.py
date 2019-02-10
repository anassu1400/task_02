from django.shortcuts import render

# Create your views here.
def resturant_view (request):
	context = {
		'msg': 'Hello World!'
	}
	return render(request, 'restaurant_template.html', context)