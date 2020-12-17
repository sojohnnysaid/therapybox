class RegisterView(CreateView):

​	model = User

​	fields = ['username', 'email', 'password']

​	 template_name = 'users/users_create.html'

