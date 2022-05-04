from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from order.views import user_orders
from shop.models import Product
from django.shortcuts import get_object_or_404, render, redirect
from .forms import SignUpForm, ProfileForm
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        profileform = ProfileForm(request.POST)

        if form.is_valid() and profileform.is_valid():
            user = form.save()

            accounts = profileform.save(commit=False)
            accounts.user = user
            accounts.save()

            login(request, user)

            return redirect('accounts:signin')
    else:
        form = SignUpForm()
        profileform = ProfileForm()

    return render(request, 'registration/signup.html', {'form': form, 'profileform': profileform})


@login_required
def get_or_create_profile(request):
    profile = None
    user = request.user
    try:
        profile, created = Profile.objects.get_or_create(user=user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user, ...)
    return render(request, 'registration/user_profile.html')


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pages:home')
            else:
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('/')


class UserEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = ['id', 'profile_image', 'dob', 'phone', 'email']
    success_url = reverse_lazy('accounts:userpage')

    def get_object(self):
        return self.request.user.profile

    def test_func(self):
        return self.request.user.profile


@login_required
def dashboard(request):
    orders = user_orders(request)
    return render(request, "registration/dashboard.html", {"section": "profile", "orders": orders})


@login_required
def wishlist(request):
    products = Product.objects.filter(users_wishlist=request.user)
    wishlist_count = Product.objects.filter(
        users_wishlist=request.user).all().count()
    context = {
        'wishlist_count': wishlist_count,
        'wishlist': products
    }
    return render(request, "registration/wishlist.html", context)


@login_required
def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    wishlist_count = Product.objects.count()
    if product.users_wishlist.filter(id=request.user.id).exists():
        product.users_wishlist.remove(request.user)
        wishlist_count -= wishlist_count
    else:
        product.users_wishlist.add(request.user)
        wishlist_count += wishlist_count
    return HttpResponseRedirect(request.META["HTTP_REFERER"])


# class SignUpView(CreateView):
#     form_class = SignUpForm
#     success_url = reverse_lazy('accounts:signin')
#     template_name = 'registration/signup.html'


""" class ProfilePageView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    success_url = reverse_lazy('accounts:signin')

    def get_object(self):
        return self.request.user

    def test_func(self):
        return self.request.user.profile """

""" 
def userpageView(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    success_url = reverse_lazy('accounts:userpage')
    return render(request=request, template_name="registration/user_profile.html", context={"user": request.user, "user_form": user_form, "profile_form": profile_form})

 """


# def userpageView(request):

#     if request.method == "POST":
#         user_form = UserForm(request.POST or None,
#                              request.FILES or None, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid():
#             user_form.save()
#             messages.success(
#                 request, ('Your profile was successfully updated!'))
#         elif profile_form.is_valid():
#             profile_form.save()
#             messages.success(
#                 request, ('Your wishlist was successfully updated!'))
#         else:
#             messages.error(request, ('Unable to complete request'))
#         return redirect("accounts:userpage")
#     user_form = UserForm(instance=request.user)
#     profile_form = ProfileForm(instance=request.user.profile)
#     return render(request=request, template_name="registration/user_profile.html", context={"user": request.user, "user_form": user_form, "profile_form": profile_form})
