from django.shortcuts import render, redirect,get_list_or_404,get_object_or_404
from django.contrib import auth
from .models import User
from news.models import NewsClass

def dashboard(request):
    if request.user.is_authenticated:
        footer_cat = NewsClass.objects.all()
        user_id = request.user.id
        user = get_object_or_404(User, id=user_id)
        if request.method == "POST" :
            cat_name = NewsClass.objects.all()
            #category_count = cat_name.count()
            cat = {}
            catx = []
            for category in cat_name:
                cat[category.title] = request.POST.get(category.title, "off")
                if cat[category.title] == "on":
                    obj = get_object_or_404(NewsClass,id=category.id)
                    user.fav_news_class.add(obj)
                    user.save()
                else:
                    obj = get_object_or_404(NewsClass, id=category.id)
                    user.fav_news_class.remove(obj)
                    user.save()

        #user.save()
        category    = NewsClass.objects.all()
        user_cat    = user.fav_news_class.all()
        ########################

        ########################
        i = 0
        cat_name = category.count()
        for x in category:
            for y in user_cat:
                x.check = ""
                x.cat_name = cat_name
        for x in category:
            for y in user_cat:
                if x == y:
                    x.check = "checked"

        context = {'category':category,'footer_cat':footer_cat,}
        return render(request, 'pages/dashboard.html',context=context)
    else:
        return redirect('login')



def login(request):
    footer_cat = NewsClass.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')
    return render(request, 'pages/login.html',{'footer_cat':footer_cat,})


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if len(password) | len(repassword) < 8:
            # messages.error(request, 'Your password is short, it must be greater than 8 characters !')
            return redirect('register')
        else:
            if password != repassword:
                # messages.error(request, 'Password does not match !')
                return redirect('register')
            else:
                if User.objects.filter(username=username).exists():
                    # messages.error(request, 'The username is token !')
                    return redirect('register')
                else:
                    if User.objects.filter(email=email).exists():
                        # messages.error(request, 'The email has registered before !')
                        return redirect('register')
                    else:
                        user = User.objects.create_user(
                            username=username, password=password, email=email, name=name,
                        )
                        user.save()
                        # messages.success(request, 'Congratulation, you are successfully registered !')
                        return redirect('login')

            return redirect('register')
    else:
        footer_cat = NewsClass.objects.all()
        context = {'footer_cat':footer_cat,}
        return render(request, 'pages/register.html',context=context)


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('index')
    else:
        return redirect('login')
