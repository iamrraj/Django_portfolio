import json

import requests
from django.views import generic
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Contact,work,blog,About
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone



def index(request):
    lol = About.objects.all()
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joker': joke, 'about' : lol}
        return render(request, 'mysite/index.html', context)
    else:
        firstname = 'Rahul '
        lastname = 'Raj '

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')

        context = {'joker': joke,'about' : lol}
        return render(request, 'mysite/index.html', context)


# def portfolio(request):
#     context = dict()
#     context['blog' ] = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis aliquid atque, nulla? Quos cum ex quis soluta, a laboriosam. Dicta expedita corporis animi vero voluptate voluptatibus possimus, veniam magni quis!'
#     return render( request, 'mysite/portfolio.html', context = context )
def portfolio(request):
    
    time = timezone.now().date()
    contact_list = blog.objects.all()
    search_term=''
    # if request.user.is_staff or request.user.is_superuser:
    #     contact_list = Post.objects.all()

    # query = request.GET.get("q")
    # if query:
    #     contact_list= Post.filter(title_iconatins=query)
    #     return render(request, 'home.html')
                      

    if 'q' in request.GET:
        search_term = request.GET['q']
        contact_list = contact_list.filter(Q(title__icontains=search_term)|
                                           Q(body__icontains=search_term)).distinct()
        

                        # Q(author=query)
                        # # ).distinct()
    paginator = Paginator(contact_list, 6) # Show 6 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'mysite/portfolio.html', {'contacts': contacts})





# class portfolio(generic.ListView):
#    # context = dict()
#    # context['blog' ] = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis aliquid atque, nulla? Quos cum ex quis soluta, a laboriosam. Dicta expedita corporis animi vero voluptate voluptatibus possimus, veniam magni quis!'
# 	template_name = 'mysite/portfolio.html'
# 	context_object_name = 'latest_question_list'

# 	def get_queryset(self):
# 		"""Return the last five published questions."""
# 		return work.objects.order_by('-pub_date')[:5]

    


class BlogDetailView(generic.DetailView):
    model = blog
    template_name = 'mysite/project.html'

class ProductDetailView(DetailView):
    model = blog
    template_name = 'mysite/project.html'

def contact(request):
    context_object_name = 'latest_question_list'

    if request.method == 'POST':
        first_r = request.POST.get( 'fname' )
        last_r = request.POST.get( 'lname' )
        phone_r = request.POST.get( 'phone' )
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(fname = first_r,lname= last_r,phone=phone_r,email=email_r, subject=subject_r, message=message_r)
        c.save()

        return render(request, 'mysite/thank.html')
    else:
        return render(request, 'mysite/contact.html')

def login(request):
   # context = dict()
   # context['blog' ] = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Reiciendis aliquid atque, nulla? Quos cum ex quis soluta, a laboriosam. Dicta expedita corporis animi vero voluptate voluptatibus possimus, veniam magni quis!'
	return render( request, 'mysite/login.html' )