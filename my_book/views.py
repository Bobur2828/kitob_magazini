from django.shortcuts import render,get_object_or_404

from .models import Book,Izoh,Status,Obuna,Category,Country, Users
import requests


def index(request):
    categorylar=list(Category.objects.all().order_by('?'))  #Slaydlarda category rasmini random xolatda olish uchun   
    category=Category.objects.order_by('name')              #Categoriyalarni cho qilish   name boyicha tartiblangan 
    booklar = Book.objects.order_by('-data_created')[:4]    #Yangi nashrlarda faqat 4 tasini chop etish
    kitob= Book.objects.order_by('print_date')[:4]          #Eng ommabop kitoblar chop etish uchun
    izohlar = list(Izoh.objects.all().order_by('?')[:6])    #Mijozlar izohlari  izohlar soni kop bolsa ham random 6 donasini olib beradi
    status=Status.objects.all()                             #Statiyalar uchun 
    obuna=Obuna.objects.all()                               #Pullik xizmatlar uchun
    data = {
        'izohlar':izohlar,
        'status':status,
        'obuna':obuna,
        'category':category,
        'booklar':booklar,
        'kitob':kitob,
        'categorylar':categorylar
    }
    
    return render(request, 'my_book/index.html', context=data)


def category(request):
    category=Category.objects.order_by('name')              #Category page kategoriyalar chop eshit uchun
    davlat=Country.objects.order_by('name')                 #Catergoriya page da  adabiyot turlari
    data = {
        'category':category,
        'davlat':davlat
    }
    return render(request, 'my_book/category_page.html', context=data)


def kitoblar(request):
    book=Book.objects.order_by('name')                      #Kitoblar  pageda  kitoblarni ism boyicha chop etish
    data = {
        'book':book,
    }
    return render(request, 'my_book/kitoblar.html', context=data)


def sotuv(request, kitob_slug):
    book=get_object_or_404(Book, slug=kitob_slug)           #Kitoblar batarfsil kirish uchun slug
    
    data = {
        'book':book,
    }

    return render(request, 'my_book/show_kitob.html', context=data)




def show_group(request, guruh_slug):                        # har hil adabiyotlar sahifasini ochish uchun 
    group = get_object_or_404(Country, slug=guruh_slug)
    books = group.literal.all()
    
    data = {
        'page':f"{group.name} adabiyotidan na'munalar ",
        'books': books,
    }
    

    return render(request, 'my_book/show_group.html', context=data)

def janr(request, janr_slug):
    janr1=get_object_or_404(Category, slug=janr_slug)       #Janrlar batafsil pagesidan slug olib 
    books = janr1.books.all()
    data = {
        'page':"Janr haqida ma'lumot ",
        'janr1':janr1,
    }

    return render(request, 'my_book/show_category.html', context=data)


def cat(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    books = Book.objects.filter(cat=category)                      #books modelidagi cat=fkeyi  mos bo'lsa oladi
    
    if not books:                                                   #books  qiymatga egaligini tekshiramiz 
        data = {
            'page': f"{category.name} janriga oid kitoblar hali mavjud emas",
            'category': category,                                   # agar book bo'sh bolsa  
        }
        return render(request, 'my_book/hatolik.html', context=data)  # xatolik qaytaradiga page ochiladi

    data = {                                                        # agar books qiymatga ega bolsa
        'page': f"{category.name} janriga bo'yicha kitoblar",       # qiymatidagi malumotlar ekranga chop etiladi
        'category': category,
        'books': books,
    }

    return render(request, 'my_book/show_category1.html', context=data)


def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/')
    else:

        return render(request, 'login/login.html')


def Register(request):
    if request.method == 'POST':
        r = request.POST
        username = r['username']
        password = r['password']
        ism = r['ism']
        fam = r['fam']
        phone = r['phone']
        birthday = r['birthday']
        address = r['address']
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect('/login/')
        else:
            user = Users.objects.create(username=username, password=password, first_name=ism, last_name=fam,
                                        phone=phone, birthday=birthday, address=address)
            login(request, user)
            return redirect('/yuklash/')

    else:
        return render(request, 'login/register.html')


def Yuklash(request):
    context = {
        'category': Category.objects.all(),
        'davlat': Country.objects.all()
    }
    if request.method == "POST":
        r = request.POST
        f = request.FILES

        category = r['category']
        photo = f['photo']
        name = r['name']
        avtor = r['avtor']
        content = r['content']
        print_date = r['print_date']
        literal = r['literal']
        pdf = f['pdf']
        slug = r['slug']

        Book.objects.create(cat_id=category, name=name, photo=photo, pdf=pdf, slug=slug, avtor=avtor, content=content,
                            print_date=print_date, literal_id=literal)

        return redirect('/')
    else:
        return render(request, 'login/yuklash.html', context)


def Logout(request):
    logout(request)
    return redirect('/login/')


def SendMsg(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']

    bot_token = '6437135033:AAHvK59HsWn_ZzDtCvNRfwARTkGQ8pRUTa0'
    text = 'Saytdan xabar: \n\nIsmi : ' + name + '\nemail : ' + email + '\nxabar : ' + message
    url = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id='
    requests.get(url + '6516071223' + '&text=' + text)

    return redirect('/')




