application = open ( "input.txt" ) 

str = application.read().split()
age = int(str[5])
role = str[8]

application.close()

def identify(age, role):
    if role == 'moderator':
        print('mdoer')
    elif age > 17  and role == "student":
        print('dogovor')
    elif age < 17 and role == "student":
        print('roditel')

identify(age, role)


