from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Userdetails,Products,Category
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from django.views.decorators.cache import cache_control


# Create your views here.



#********USER REGIDTRATION***************************************
@cache_control(no_cache=True)
def user_signup(request):
    if request.method == 'POST':
        uname = request.POST.get('user_name')
        uemail = request.POST.get('user_email')
        upassword1 = request.POST.get('user_password1')
        upassword2 = request.POST.get('user_password2')
        if upassword1 != upassword2:
            return HttpResponse('retype the password')
        else:
            my_user = Userdetails.objects.create(user_name=uname,user_email=uemail,user_password=upassword1)
            my_user.save()
            return redirect('user_login')
    else:
        print('not post')
        return render(request,'user_signup.html')



#########################################################
def admin_dashboard(request):
    return render(request,'aadmin_dashboard.html')



#*****USER LOGIN**********************************************************
@cache_control(no_cache=True)
def user_login(request):
    if 'user_email' in request.session:
        return redirect('index_3_home')
    if request.method == "POST":
        uemail=request.POST['user_email']
        upassword=request.POST['user_password']
        user=Userdetails.objects.get(user_email=uemail,user_password=upassword)
        if user is not None:
            if user.u_active:
                request.session['user_email'] = uemail
                return render(request,'index_3_home.html')
            else:
                u_blocked =' You are blocked !!!!!!!!!'
                return render(request,'user_login.html',{'u_blocked': u_blocked})


        else:
            return HttpResponse('PASSWORD INCORRECT')
    
    
    return render(request,'user_login.html')



def user_logout(request):
    if 'user_email' in request.session:
        del request.session['user_email']
    return redirect('user_login')



@cache_control(no_cache=True)
def admin_login(request):
    error_msg = None
    if 'name' in request.session:
        return redirect('admin_dashboard')

    # if request.method == 'GET':
    #     if request.user.is_authenticated:
    #         return redirect('admin_userlist')
    #     return render(request, 'admin_login.html')
    # elif request.user.is_authenticated:
    #     return redirect('admin_dashboard')
    # else:
    if request.method == 'POST':
            name = request.POST.get('name')
            password = request.POST.get('password')
            user = authenticate(request,username =name, password=password)
            if user is not None:
                request.session['name'] = name
                return redirect('admin_dashboard')
            else:
                error_msg = 'invalid Name or password..!'
    return render(request, 'admin_login.html', {'error': error_msg})



@cache_control(no_cache=True)
def admin_logout(request):
    if 'name' in request.session:
        del request.session['name']
        return redirect('admin_login')

        



@cache_control(no_cache=True)
def admin_logout(request):
        logout(request)
        return redirect('admin_login')



@cache_control(no_cache=True)
def admin_userlist(request):
    if request.user.is_authenticated:
        userlist = Userdetails.objects.all().order_by('id')
        return render(request,'admin_userlist.html',{'tablelist' : userlist})





@cache_control(no_cache=True)
def admin_products(request):
    if 'email' in request.session:
        return render(request,'admin_productslist.html')



@cache_control(no_cache=True)
def admin_addproducts(request):
    
        if request.method == 'POST' :
            book_title = request.POST.get('book_title')
            author = request.POST.get('author')
            picture = request.FILES.get('myfile')
            description = request.POST.get('description')
            p_category = request.POST.get('category')
            price = request.POST.get('price')
            category = Category.objects.filter(cate_name=p_category).first()
            Products.objects.create(book_title=book_title,author=author,picture=picture,description=description,price=price,p_category=category)    
            return redirect('admin_productslist')
        else:
            pr_cate=Category.objects.all()
            return render(request,'admin_addproducts.html',{'pr_cate' : pr_cate})




@cache_control(no_cache=True)
def admin_productslist(request):
    #if 'email' in request.session:
        list =Products.objects.all()
        return render(request,'admin_productslist.html',{'list' : list})

def admin_deleteproduct(request):
    uid = request.GET['uid']
    del_pro = Products.objects.filter(id = uid)
    del_pro.delete()
    return redirect('admin_productslist')




@cache_control(no_cache=True)
def shop_list_left_books(request):
    list =Products.objects.all()
    return render(request,'shop-list-left-books.html',{'list' : list})



@cache_control(no_cache=True)
def product_details(request):
    list =Products.objects.all()
    return render(request,'product_details.html',{'list' : list})



#@cache_control(no_cache=True)
def index_3_home(request):
    if 'user_email' in request.session:
        return render(request,"index_3_home.html")
    return redirect('user_login')


def admin_addcategory(request):
    if request.method == 'POST':
        add_category = request.POST.get('category')
        Category.objects.create(cate_name = add_category)
        return redirect('admin_categorylist')
    pr_cate = Category.objects.all()
    return render(request,'admin_addcategory.html',{'pr_cate' : pr_cate})




def admin_editcategory(request):
    if request.method =='POST':
        uid =request.GET['uid']
        category = request.POST.get('category')
        Category.objects.filter(id=uid).update(cate_name=category)
        return redirect('admin_categorylist')
    else:
        return render(request,'admin_editcategory.html')


def admin_deletecategory(request):
    uid =request.GET['uid']
    cat_del = Category.objects.filter(id=uid)
    cat_del.delete()
    return redirect('admin_categorylist')





def admin_categorylist(request):
    p_cate = Category.objects.all()
    return render(request,'admin_categorylist.html',{'p_cate' : p_cate})


def userblock(request):
    print("!!!!Inside")
    uid = request.GET['uid']
    should_block = Userdetails.objects.filter(id=uid)
    for i in should_block:
        if i.u_active:
            Userdetails.objects.filter(id = uid).update(u_active = False)
        else:
             Userdetails.objects.filter(id = uid).update(u_active = True)
    return redirect('admin_userlist')



def admin_updateuser(request):
    if request.method == 'POST':
        id=request.GET['uid']
        uname = request.POST.get('user_name')
        uemail = request.POST.get('user_email')
        upassword1 = request.POST.get('user_password1')
        upassword2 = request.POST.get('user_password2')
        if upassword1 != upassword2:
            error='Password mismaching'
            return render(request,'admin_updateuser.html',{'error' : error})
        else:
            Userdetails.objects.filter(id=id).update( 
                user_name = uname,
                user_email = uemail,
                user_password = upassword1
            )
            return redirect('admin_userlist')
    return render(request,'admin_updateuser.html')


def admin_editproducts(request):
    if request.method == 'POST':
        uid = request.GET['uid']
        book_title = request.POST.get('book_title')
        author = request.POST.get('author')
        picture = request.FILES.get('myfile')
        description = request.POST.get('description')
        p_category = request.POST.get('category')
        price = request.POST.get('price')
        category = Category.objects.filter(cate_name=p_category).first()
        Products.objects.filter(id=uid).update(
            book_title = book_title,
            author = author,
            description = description,
            price =price,
            picture = picture,
            p_category =category
        )
        return redirect('admin_productslist')
    p_cate = Category.objects.all()
    return render(request,'admin_editproducts.html',{'p_cate' : p_cate})




        

  


