from django.conf import settings
from django.core.mail import send_mail

def Send_Verification_Email(email, token):

    subject = 'Wellcome to Advance Django Authentication System'
    message = f"""Wellcome to Advance Django Authentication System, You have Registered An Account With This Email. 
                To Activate Your Account Please Click To This Link: http://127.0.0.1:8000/accounts/authtoken/{token}"""
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    return send_mail( subject, message, email_from, recipient_list )


def Send_Password_Reset_Email(email, token):

    subject = 'Password Reset For Django Authentication System'
    message = f"""Wellcome to Advance Django Authentication System, You have Registered An Account With This Email. 
                To Reset The Password of Your Account Please Click To This Link: http://127.0.0.1:8000/accounts/resetokenpass/{token}"""
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    return send_mail( subject, message, email_from, recipient_list )