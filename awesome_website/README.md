# User management

## Send e-mail throught Django

https://mailtrap.io/blog/django-send-email/https://mailtrap.io/blog/django-send-email/https://mailtrap.io/blog/django-send-email/
https://ordinarycoders.com/blog/article/django-password-reset

If django seems not sending e-mails try to verify if your user account have an e-mail.

```python
# settings.py, it must be at end of file.
#                                          filebased
#                                          smtp
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = '127.0.0.1'
EMAIL_PORT = 25
EMAIL_FILE_PATH = BASE_DIR / 'emails'
```

```shell
# Python smtp server to test if django is sending e-mails.
$ sudo python3 -m smtpd -c DebuggingServer -n 127.0.0.1:25
```

```python
# Python code, independent of django, to see if smtp is working.

import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except smtplib.SMTPException:
   print ("Error: unable to send email")
```

## Sort of installed apps

Your apps must be installed first, cause if not django will use default templates.
And you want use your: 'users/templates/registration'.
