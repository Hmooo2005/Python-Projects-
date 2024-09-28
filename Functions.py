# def say_hello():
#     print ('Hello World!')

# say_hello()

#=======================================================

# def                   ---->  key word of functions
# say_hello             ---->  Function name
# print ('Hello World!')---->  Task of the Function

#=======================================================

# def say_hello():
#     return 'Hello World!'

# say_hello() # nothing happen to show the function store it in variable
# great_user = say_hello()
# print(great_user)

#==========================================================

# def say_hello(name):
#     print (f'Hello {name}')

# say_hello('mosa')

#==========================================================

# name is called {parameter}
# mosa is called {Argument}
print('#'*50)
#==========================================================

# def great_male_user(name):
#     print(f'Hello Mr.{name} How are You')

# def great_female_user(name):
#     print(f'Hello Mis.{name} How are You')

# name = input('Please enter Your name: ')
# gender = input("please right Your Gender male/female: ").lower()

# if gender == 'male':
#     great_male_user(name)
# elif gender == 'female':
#     great_female_user(name)
# else:
#     print('please enter one of the two gender!')

#==========================================================

# def say_hello(*name): #unpacking arguments
#     for b in name:
#         print (f'Hello {b}')

# my_list = []
# num_of_names = int(input("How many names You want to enter: "))
# for x in range(num_of_names):
#     name = input('Please enter Your name: ')
#     my_list.append(name)

# say_hello(*my_list)

#==========================================================

# def say_hello(name,age ,country = 'UnKnown'): # Default Parameter
#     print(f'Hello {name} Your age is {age} and You are From {country} is That Right?')

# say_hello('mohammed',20)

#==========================================================

def say_hello(name):print (f'Hello {name}')

hello = lambda name : f'Hello {name}'
#       lambda {parameter name} : Task of the Function

# say_hello('mosa')
# print(hello('mostafa'))

#==========================================================

list_of_users = ['mohammed' , 'mosa', 'khawla', 'gmal', 'ahmed']

def check_user(name):
    if name in list_of_users:
        return f'Hello {name}'
    else:
        print('Sorry You are not a user :(')
        add_choice = input('Do you want to add to users? y/n? ').lower()
        if add_choice == 'n':
            quit()
        elif add_choice == 'y':
            add_new_user = input("Please enter Your name: ")
            list_of_users.append(add_new_user)
            print('You Have added!')
            check = input('Do you want to check if you Have added? y/n? ').lower()
            if check == 'n':
                quit()
            elif check == 'y':
                print(list_of_users)
            else:
                print('invalid input :(')
                quit()
        else:
            print('invalid input :(')
            quit()
# print(check_user('Hitham'))

#==========================================================