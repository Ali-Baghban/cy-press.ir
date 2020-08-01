from django.shortcuts import render,get_object_or_404
from account.models import User
from news.models import NewsClass
from .models import About,Contact

def about(request):
    footer_cat = NewsClass.objects.all()
    about = About.objects.first()
    context = {'about':about,'footer_cat':footer_cat}
    return render(request,'pages/about.html', context=context)

def contact(request):
    footer_cat = NewsClass.objects.all()
    if request.user.is_authenticated:
        user_id = request.user.id
        user    = get_object_or_404(User, id=user_id)
        context ={'user':user}
        return render(request, 'pages/contact.html',context=context)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        contact = Contact.objects.create_user(
                            name=name, email=email, comment=comment,
                        )
        contact.save()
    context = {'footer_cat':footer_cat,}
    return render(request, 'pages/contact.html')