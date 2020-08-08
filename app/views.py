from django.shortcuts import render, reverse, redirect
from django.views.generic import View, DetailView, ListView
from .models import Item
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from .forms import UserForm

class IndexView(View):
	def get(self, request):
		all = Item.objects.all()
		new = all[0::-1]

		if len(new) > 7:
			new = new[0:8]
		else:
			new = new[0:]

		popular = Item.objects.filter(label='P')
		contex = {'all':all,
				  'popular':popular,
				  'new':new
				}
		return render(request, "app/index.html", contex )


class SportsView(View):
	def get(self, request):
		popular = Item.objects.filter(label='P',category='S')
		Items = Item.objects.filter(category='S')
		new = Item.objects.filter(label='S', category='S')
		return render(request, "app/sports.html", {
		'popular':popular,
		'Items':Items,
		'new':new
		})

class HealthView(View):
	def get(self, request):
		
		Items = Item.objects.filter(category='H')
		return render(request, "app/health.html", {"Items":Items})

class BooksView(View):
	def get(self, request):
		
		Items = Item.objects.filter(category='B')
		return render(request, "app/books.html", {"Items":Items})

class MFashionView(View):
	def get(self, request):
		
		Items = Item.objects.filter(category='MF')
		return render(request, "app/men_fashion.html", {"Items":Items})

class PhonesTabletsView(View):
	def get(self, request):
		
		Items = Item.objects.filter(category='PH')
		return render(request, "app/phonestablets.html", {"Items":Items})

class WFashionView(View):
	def get(self, request):
		
		Items = Item.objects.filter(category='WF')
		return render(request, "app/women_fashion.html", {"Items":Items})

class KidsView(View):
	def get(self, request):
		
		Items = Item.objects.filter(category='K')
		return render(request, "app/kids.html", {"Items":Items})

class CamerasView(View):
	def get(self, request):
		
		Items = Item.objects.filter(category='CM')
		return render(request, "app/cameras.html", {"Items":Items})

class ElectronicsView(View):
	def get(self, request):
	
		Items = Item.objects.filter(category='E')
		return render(request, "app/electronics.html", {"Items":Items})

class PrivacypolicyView(View):
	def get(self, request):
		return render(request, "app/privacypolicy.html")

class TermsofuseView(View):
	def get(self, request):
		return render(request, "app/termsofuse.html")

class AboutUsView(View):
	def get(self, request):
		return render(request, "app/aboutus.html")
		
class ContactUsView(View):
	def get(self, request):
		return render(request, "app/contactus.html")
				
				
class ItemDetailView(DetailView):
    model = Item
    template_name = "app/product.html"
	
	
class SearchView(ListView):

	def get(self, request):
		all = Item.objects.all() 
		search = request.GET.get("search_title")
		category = request.GET.get("category")

		
		if search != '' and search is not None:
			all = all.filter(title__icontains=search)
			
		if category != '' and category is not None:
			all = all.filter(category__icontains=category)

		contex = {'all':all}

		return render(request, "app/search.html", contex )

class SignupView(View):
	form_class = UserForm
	template_name = 'registration/signup.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			
			user.set_password(password)
			user.save()

			# if Credential are correct
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('app:index')
		return render(request, self.template_name, {'form':form})

