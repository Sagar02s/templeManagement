from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login as dj_login, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

from eSeveTickets.models import Company, State

# Create your views here.
def home(request):
    return render(request, 'index.html')

def userlogin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    else:
        if request.method =="POST":
            uname = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(request,username=uname,password=passwd)
            if user:
                dj_login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.error(request,"Invalid Credentials")
                return render(request,'login.html')
        else:
            return render(request,'login.html')
        
        
        
@login_required(login_url='userlogin')
def userlogout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('userlogin'))


@login_required(login_url='userlogin')
def immovable(request):
    return render(request,'immovable.html')

@login_required(login_url='userlogin')
def movable(request):
    return render(request,'movable.html')


@login_required(login_url='userlogin')
def incExp(request):
    return render(request,'incExp.html')

@login_required(login_url='userlogin')
def kaanike(request):
    return render(request,'kaanike.html')

@login_required(login_url='userlogin')
def masters(request):
    return render(request,'masters.html')

@login_required(login_url='userlogin')
def poojaReport(request):
    return render(request,'poojaReport.html')


@login_required(login_url='userlogin')
def provision(request):
    return render(request,'provision.html')

@login_required(login_url='userlogin')
def seva(request):
    sevas= [
        {"Name":"Alankar","kannada":"ಅಲಂಕಾರ","price":"₹500"},
        {"Name":"Alankar","kannada":"ಅಲಂಕಾರ","price":"₹500"},
        {"Name":"Alankar","kannada":"ಅಲಂಕಾರ","price":"₹500"},
        {"Name":"Alankar","kannada":"ಅಲಂಕಾರ","price":"₹500"},
        {"Name":"Alankar","kannada":"ಅಲಂಕಾರ","price":"₹500"},
        {"Name":"Alankar","kannada":"ಅಲಂಕಾರ","price":"₹500"},
        {"Name":"Alankar","kannada":"ಅಲಂಕಾರ","price":"₹500"},
        {"Name":"Alankar","kannada":"ಅಲಂಕಾರ","price":"₹500"},
        {"Name":"Alankar","kannada":"ಅಲಂಕಾರ","price":"₹500"},
        {"Name":"Alankar","kannada":"ಅಲಂಕಾರ","price":"₹500"},
        {"Name":"Alankar","kannada":"ಅಲಂಕಾರ","price":"₹500"},
        {"Name":"Alankar","kannada":"ಅಲಂಕಾರ","price":"₹500"}

        ]
    return render(request,'seva.html',{'sevas':sevas})

@login_required(login_url='userlogin')
def userReport(request):
    return render(request,'userReport.html')

@login_required(login_url='userlogin')
def profile(request):
    states = State.objects.all()  # Get all states for the dropdown
    
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        address = request.POST.get('address')
        state_id = request.POST.get('state')
        pincode = request.POST.get('pincode')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        currency_symbol = request.POST.get('currency_symbol')
        maintain = request.POST.get('maintain')
        financial_year = request.POST.get('financial_year')
        gstin = request.POST.get('gstin')
        st = request.POST.get('st')
        pan = request.POST.get('pan')
        cin_llp = request.POST.get('cin_llp')
        serial_option = request.POST.get('serial_option')
        purchase_date = request.POST.get('purchase_date')
        sales_due = request.POST.get('sales_due')

        # Validation (basic)
        if not all([company_name, address, pincode, phone_number, email, currency_symbol, maintain, financial_year,
                    gstin, st, pan, cin_llp, serial_option, purchase_date, sales_due]):
            return render(request, 'company_form.html', {'error': 'All fields are required.', 'states': states})

        # Convert state_id to a State object
        state = State.objects.get(id=state_id)

        # Create the Company object
        company = Company.objects.create(
            company_name=company_name,
            address=address,
            state=state,
            pincode=pincode,
            phone_number=phone_number,
            email=email,
            currency_symbol=currency_symbol,
            maintain=maintain,
            financial_year=financial_year,
            gstin=gstin,
            st=st,
            pan=pan,
            cin_llp=cin_llp,
            serial_option=serial_option,
            purchase_date=purchase_date,
            sales_due=sales_due
        )

        return redirect('company_success')  # Redirect to a success page after saving

    return render(request, 'profile.html', {'states': states})