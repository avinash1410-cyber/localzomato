from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import Restaurants
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .forms import RestaurantsForm
from django.views import View
from django.utils import timezone
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib.auth.decorators import login_required



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout












def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('home')  # Replace 'home' with the actual name of your home page
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'restaurants/login.html', {'form': form})






def custom_logout(request):
    logout(request)
    return redirect('home')  # Replace 'home' with the actual name of your home page






def Home(request):
    salary = 12 * 60000
    context = {
        'name': 'Avinash',
        'age': 23,
        'Location': "Delhi",
        'salary': salary,
        'members': ["Ashish", "Sudha", "Saroja", "Sarita"],
        'no':[7,6,3,3,4,7,3,2]
    }

    return render(request, 'Home.html', context=context)


def About(request):
    salary = 12 * 60000
    context = {
        'name': 'Avinash',
        'age': 23,
        'Location': "Delhi",
        'salary': salary,
        'members': ["Ashish", "Sudha", "Saroja", "Sarita"],
        'no':[7,6,3,3,4,7,3,2]
    }

    return render(request, 'About.html', context=context)



def Contact(request):
    salary = 12 * 60000
    context = {
        'name': 'Avinash',
        'age': 23,
        'Location': "Delhi",
        'salary': salary,
        'members': ["Ashish", "Sudha", "Saroja", "Sarita"],
        'no':[7,6,3,3,4,7,3,2]
    }

    return render(request, 'Contact.html', context=context)





class HomeView(TemplateView):
    template_name = 'Home.html'

    def get_context_data(self, **kwargs):
        salary = 12 * 60000
        context = {
            'name': 'Avinash',
            'age': 23,
            'Location': "Delhi",
            'salary': salary,
            'members': ["Ashish", "Sudha", "Saroja", "Sarita","Class"],
            'no': [7, 6, 3, 3, 4, 7, 3, 2],
        }
        return context
    


# class RestaurantsView(TemplateView):
#     template_name = 'restaurants/restaurants_list.html'

#     def get_context_data(self, **kwargs):
#         restaurants = Restaurants.objects.all()
#         context = {
#             'Restaurants_list': restaurants
#         }
#         return context



class RestaurantListView(ListView):
    model = Restaurants
    template_name = 'restaurants/restaurant_list.html'
    context_object_name = 'restaurants'
    ordering = ['name']  # Specify the ordering of the list

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug is None:
            return Restaurants.objects.all()

        queryset = Restaurants.objects.filter(
            Q(category__icontains=slug) | Q(location__icontains=slug) | Q(name__icontains=slug)
        )

        # Use get_object_or_404 to raise a 404 if no matching Restaurants are found
        # get_object_or_404(queryset)

        return queryset


class RestaurantDetailView(DetailView):
    model = Restaurants
    template_name = 'restaurants/restaurant_detail.html'
    context_object_name = 'restaurant'







@login_required(login_url='/login/')
def add_restaurant(request):
    template_name = 'restaurants/restaurant_form.html'  # Update with the correct template path

    if request.method == 'GET':
        form = RestaurantsForm()
    elif request.method == 'POST':
        form = RestaurantsForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                instance=form.save(commit=False)
                instance.user=request.user
                instance.save()
                return redirect('restaurant_list')  # Update with the correct view name
    return render(request, template_name, {'form': form})






# class AddRestaurantView(LoginRequiredMixin, FormView):
#     template_name = 'restaurants/restaurant_form.html'  # Update with the correct template path
#     form_class = RestaurantsForm
#     success_url = '/restaurant_list'  # Update with the correct view name
#     login_url = '/admin/'

#     def form_valid(self, form):
#         form.instance.user = self.request.user  # Assign the current user to the user field
#         if super().form_valid(form):
#             form.save()
#             return redirect('/restaurant_list')
#         else:
#             return redirect('/admin/')
    


# class AddRestaurantView(LoginRequiredMixin, View):
#     template_name = 'restaurants/restaurant_form.html'  # Update with the correct template path

#     def get(self, request, *args, **kwargs):
#         form = RestaurantsForm()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = RestaurantsForm(request.POST)
#         if form.is_valid():
#             restaurant = form.save(commit=False)
#             restaurant.user = request.user  # Assign the current user to the user field
#             restaurant.save()
#             return redirect('restaurant_list')  # Update with the correct view name
#         return render(request, self.template_name, {'form': form})

    



# class AddRestaurantView2(View):
#     template_name = 'restaurants/add_restaurant.html'  # Update with the correct template path

#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name)

#     def post(self, request, *args, **kwargs):
#         # Extract data from the request
#         name = request.POST.get('name')
#         location = request.POST.get('location')
#         category = request.POST.get('category')

#         # Create a new Restaurants instance and save it
#         restaurant = Restaurants(name=name, location=location, category=category, created_at=timezone.now())
#         restaurant.save()

#         return redirect('restaurant_list')  # Update w 
    


# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView
# from .models import Restaurants
# from django.utils import timezone

# class AddRestaurantView(CreateView):
#     model = Restaurants
#     template_name = 'restaurants/add_restaurant.html'  # Update with the correct template path
#     fields = ['name', 'location', 'category']
#     success_url = reverse_lazy('restaurant_list')  # Update with the correct view name

#     def form_valid(self, form):
#         form.instance.created_at = timezone.now()
#         return super().form_valid(form)
