from twilio.rest import Client

def send_otp_via_sms(phone_number, otp):
    account_sid = 'ACccf0994b6176348f52352dd2fa2cf87c'
    auth_token = 'e7cd811bb46b38b7c1261d1500cce9cf'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+12673184725',
    body=f'Your reset password OTP is : {otp}',
    to=phone_number
    )

    print(message.sid)