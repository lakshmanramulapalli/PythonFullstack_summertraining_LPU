from oop.student import Student

cnm = input('College name: ')
cad = input('College addr: ')
depts = input('Department: ')
rno = int(input('Roll no: '))
snm = input('Student name: ')
sdept = input('Stud dept: ')
phno = int(input('Phone no: '))
m1 = int(input('Mark 1: '))
m2 = int(input('Mark 2: '))
m3 = int(input('Mark 3: '))

stud = Student(cname=cnm, caddr=cad, rno=rno, noofdepts=depts, sname=snm, sdept=sdept, sph=phno, m1=m1, m2=m2, m3=m3)

stud.display_collegeinfo()
#stud.calc_averege()

print(f'Stu Rno : {stud.rno}, Name : {stud.sname}, Dept: {stud.sdept}, Avereage score: {stud.calc_average()}')