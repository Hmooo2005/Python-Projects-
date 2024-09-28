class Member:

    def __init__(self, first_name, second_name, third_name, gender) :

        self.fname = first_name

        self.mname = second_name

        self.lname = third_name

        self.gender = gender

    def get_full_name(self):

        return f'{self.fname} {self.mname} {self.lname}'

    def name_with_title(self):

        if self.gender == 'male':

            return f'Hello Mr.{self.fname}'
        
        elif self.gender == 'female':

            return f'Hello Ms.{self.fname}'
        
        else:

            return f'Hello {self.fname}'

    def get_all_info(self):

        return f'{self.name_with_title()} Your Full name is {self.get_full_name()} and Your Gender is {self.gender}'


user = Member('mosa', 'ibrahim', 'mohammednor', 'male')
print(user.get_all_info())