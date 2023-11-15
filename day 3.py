import re
dict={}
first_name=input("please enter your first name :")
dict.update({"firstname":first_name})
last_name=input("please enter your second name: ")
dict.update({"lasttname":last_name})
email=input("please enter your email:")

# email
is_email=re.fullmatch(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",email)
if is_email:
    print("this is a valid email")
    dict.update({"Email":email})
else:
     print("this is not a valid email")
     email=input("please enter valid email:")
     dict.update({"Email":email})

# password
password=input("please enter your password :")
if len(password)>8:
     print("this is a valid password")
     dict.update({"PASSWORD":password})
else:
     print("this is not a valid password")
     password=input("please enter your password :")
     dict.update({"PASSWORD":password})

#phone number
mobile_phone=input("please enter your mobile phone :")
is_mobile=re.fullmatch(r"^01[0125][0-9]{8}$",mobile_phone)
if is_mobile:
     print("this is  a valid phone number")
     dict.update({"MOBILE NUMBER":mobile_phone})
else:
     print("this is not a valid phone number")
     mobile_phone=input("please enter your mobile phone :")
     dict.update({"MOBILE NUMBER":mobile_phone})


     
print(dict)
while True:
 user_email=input("please enter your email:")
 if user_email in dict ["Email"]:
  print ("valid email")
  x=dict["Email"].index(user_email)
  while True:
    user_password=input("please enter your password:")
    if user_password in dict ["PASSWORD"]:
        y=dict["PASSWORD"].index(user_password)
        if x==y:
         print("valid password")
         break
        else:
         print("unvalid password")
  break
 else:
    print ("unvalid email")