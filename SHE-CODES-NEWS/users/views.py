from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CreateAccountView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'users/createAccount.html'

class ProfileView(generic.DetailView):
	model = CustomUser
	template_name = 'users/viewAccount.html'
	context_object_name = 'profile'

class EditAccountView(generic.UpdateView):
	model = CustomUser
	form_class = CustomUserChangeForm
	template_name = 'users/editAccount.html'
	context_object_name = 'editAccount'
	def get_success_url(self):
		return reverse_lazy('users:profile', kwargs={'pk': self.object.id})
