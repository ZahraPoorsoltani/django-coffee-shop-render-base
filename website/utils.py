from django.contrib import messages


def add_err(request,form_err):
    error_persian ={  
        "The two password fields didn’t match.":
        "دو فیلد پسورد با تایید پسورد تطابق ندارند.",
        "This password is too short. It must contain at least 8 characters.":
        "پسورد خیلی کوتاه است. حداقل طول پسورد باید ۸ کاراکتر باشد.",
        "This password is too common.":
        "این پسورد خیلی رایج است",
        "This password is entirely numeric.":
        "پسورد نباید تمام عدد باشد",
        "Your password can’t be too similar to your other personal information.":
        " پسورد شما نباید شبیه به سایر اطلاعات شخصی شما باشد",
        "A user with that username already exists.":
        "این نام کاربری از قبل وجود دارد",
        "email address already exists!":
        "این ایمیل از قبل وجود دارد",
        "Enter a valid email address.":
        "ایمیل معتبر نیست."

        }
    form_field_persian = {
        'password':'پسورد',
        'password2':'تایید پسورد',
        'username':'نام کاربری',
        'email':'ایمیل',
        'captcha':'کپتچا'
    }
    err = form_err.items()
    for key,vals in err:
        for v in vals:
            if p:= error_persian.get(v,0):
                messages.add_message(request,messages.ERROR,form_field_persian[key]
                                     +': '+p)
            else:
                messages.add_message(request,messages.ERROR,form_field_persian[key]
                                     +': '+v)