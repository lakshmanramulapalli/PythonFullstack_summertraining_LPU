from oop.bikes import Bikes

brnd = input('Brand: ')
bknm = input('Bike name: ')
rpd = int(input('Rent: '))

bkobj = Bikes(brand=brnd, rent=rpd, bkname=bknm)

days = int(input('No of Days: '))
print(f'The Rent of Bike {bkobj.bikename} for {days} is {bkobj.calculate_rent(days)}')
