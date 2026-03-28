from django.shortcuts import render,redirect
from .models import Order

def index(request):
    return render(request,'index.html')

def frames(request):
    return render(request,'frames.html')

def frame_order(request):
    return render(request,'frame_order.html')

def mugs(request):
    return render(request,'mugs.html')

def keychains(request):
    return render(request,'keychains.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def thankyou(request):
    return render(request,'thankyou.html')


from django.shortcuts import render,redirect
from .models import Order

def order(request):

    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        product = request.POST.get("product_type")
        frame = request.POST.get("frame")
        size = request.POST.get("size")
        keychain = request.POST.get("keychain")
        message = request.POST.get("message")
        note = request.POST.get("note")

        photo1 = request.FILES.get("photo1")
        photo2 = request.FILES.get("photo2")

        Order.objects.create(
            name=name,
            phone=phone,
            email=email,
            product_type=product,
            frame=frame,
            size=size,
            keychain=keychain,
            message=message,
            note=note,
            photo1=photo1,
            photo2=photo2
        )

        return redirect("thankyou")

    return render(request,"order.html")
from django.shortcuts import render,redirect
from .models import Register

def register(request):

    if request.method == "POST":

        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        address=request.POST.get("address")
        password=request.POST.get("password")

        Register.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            password=password
        )

        return redirect("login")

    return render(request,"register.html")

def login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        from .models import Register

        user = Register.objects.filter(email=email, password=password)

        if user:
            request.session["user"] = email
            return redirect("index")

    return render(request,"login.html")

def logout(request):
    request.session.flush()
    return redirect("login")

