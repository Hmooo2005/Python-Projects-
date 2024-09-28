class physics:

    def __init__(self,value, determineunit='m'):

        self.value = value

        self.determineunit = determineunit

    def length(self):

        if self.determineunit == 'm':
            return f'{self.value} m'
        
        else:
            print("determine by Meter(m)")
            if self.determineunit == 'km':
                length_in_meter = self.value * 1000
            elif self.determineunit == 'dm':
                length_in_meter = self.value / 10
            elif self.determineunit == 'sm':
                length_in_meter = self.value / 100
            elif self.determineunit == 'mm':
                length_in_meter = self.value / 1000
            elif self.determineunit == 'micro':
                length_in_meter = self.value / (10**6)
            elif self.determineunit == 'A':
                length_in_meter = self.value / (10**10)
            else:
                return 'please enter a write self.value'
            return length_in_meter



    # def wight(self.value, self.determineunit ='kg'):
    #     if self.determineunit == 'kg':
    #         print(f'{self.value} kg')
    #     else:
    #         print("determine by Kilogram(kg)")
    #         if self.determineunit == 'g':
    #             length_in_kg = self.value / 1000
    #         elif self.determineunit == 'mg':
    #             length_in_kg = self.value / (10**6)
    #         elif self.determineunit == 'microgram':
    #             length_in_kg = self.value / (10**9)
    #         elif self.determineunit == 'pound':
    #             length_in_kg = float(self.value) * 0.453
    #         else:
    #             print('please enter a write self.value')
    #         print(length_in_kg)


    # def time(value, self.determineunit ='s'):
    #     if self.determineunit == 's':
    #         print(f'{self.value} s')
    #     else:
    #         print("determine by Seconds(s)")
    #         if self.determineunit == 'y':
    #             length_in_second = self.value * 12 * 30 * 7 * 24 * 3600
    #         elif self.determineunit == 'm':
    #             length_in_second = self.value * 30 * 7 * 24 * 3600
    #         elif self.determineunit == 'w':
    #             length_in_second = self.value * 7 * 24 * 3600
    #         elif self.determineunit == 'd':
    #             length_in_second = self.value * 24 * 3600
    #         elif self.determineunit == 'h':
    #             length_in_second = self.value * 3600
    #         elif self.determineunit == 'min':
    #             length_in_second = self.value * 60
    #         elif self.determineunit == 'mls':
    #             length_in_second = self.value / (10**3)
    #         elif self.determineunit == 'micro':
    #             length_in_second = self.value / (10**6)
    #         elif self.determineunit == 'nano':
    #             length_in_second = self.value / (10**9)
    #         else:
    #             print('please enter a write self.value')
    #         print(length_in_second)


    def speed():
        pass
    def distance():
        pass
# def wight():
#     pass
# def wight():
#     pass
# def wight():
#     pass




# choose_opperater = input(" ")
length1 = physics(40, 'km')
print|(length1.value)
# wight(40,'pou')