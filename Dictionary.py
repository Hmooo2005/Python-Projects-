user = {
    'name':'mohammed',
    'family name' : 'Ajeel',
    'age':20,
    'study':'university',
    'level of study' : '2nd level',
    'statue':'single',
    'work befor' : True
}

# for profile in user:
#     if len(profile) == 14 :
#         print(f'#{profile} ====>  {user[profile]}')
#     else:
#         space = 14 - len(profile)
#         print(f'#{profile}{" "*space} ====>  {user[profile]}')
        
#======================================================================
user_info = {
    'personal info' : {
        'name' : {
            '1st name' : 'Mohammed',
            '2nd name' : 'Ibrahim',
            '3rd name' : 'MohammedNour',
            '4th name' : 'Ajeel'
        },
        'age' : 18,
        'statue' : 'Single',
        'working' : False,
    },
    'Education Inof' : {
        'Primary School' : {
            'name' : "Algabas",
            'Period of Study' : '1st class to 8th class',
            'Grade of Graduation' : 277
        },
        'Secondary School' : {
            'name' : "Aletsam",
            'Period of Study' : '1st class to 3th class',
            'Grade of Graduation' : 87.9
        },
        'University' : {
            'name' : "Kassala University",
            'Period of Study' : '1st class to Now',
            'Grade of Graduation' : None
        }
    }
}

# print(user_info['personal info']['name']['1st name'])

print(' 1 '.center(50,"#"))

print(user_info.keys()) # print the keys

print(' 2 '.center(50,"#"))

print(user_info.values()) # print the values

print(' 3 '.center(50,"#"))

user2 = user_info.copy() # make a shallow copy

print(' 4 '.center(50,"#"))

print(user_info.get('personal info')) # give the value of the key. if the key do not excest give None

print(' 5 '.center(50,"#"))

a = ('name', 'age', 'statues')
b = 20
print(user_info.fromkeys(a,b)) # make keys from a and give every key the values of b

print(' 6 '.center(50,"#"))

user_info.update({'family':10}) # update the dict

print(' 7 '.center(50,"#"))

print(user.setdefault('bro','mosa')) # if key excist it will print mosa if not it will add it to the dict
print(user)

print(' 8 '.center(50,"#"))

user.pop('name') # remove the writeen key and it's value from dict

print(' 9 '.center(50,"#"))

print(user.popitem()) # give you the last key+value that added to the dict

print(' 10 '.center(50,"#"))

print(user.items()) # will print all the dict in alist it's elements are Tuples(key,value)
print(type(user.items()))
print(type(user))

print(' 11 '.center(50,"#"))

user_info.clear() # Clear the Dict
print(user_info)

