from django.shortcuts import render
import pyotp
from .forms import *
from .otps import send_otp_via_sms

# Create your views here.
def generate_otp():
    # Generate a random secret key
    secret = pyotp.random_base32()

    # Create an OTP object
    totp = pyotp.TOTP(secret, digits=4)

    # Generate the OTP
    otp = totp.now()

    return otp


def register(request):
    if request.method == "POST":
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            phone = forms.cleaned_data['phone']
            otp = generate_otp()
            send_otp_via_sms(phone, otp)
        else:
            print('Invalid form data')
    return render(request, 'signup.html')


# def verify_otp(phone, otp):
#     user = User.object.get(phone=phone)
#     if user.exists():
#         if user.otp == otp:







def signin(request):
    return render(request, 'login.html')