import measures

var= int(input('Press 1 for Square, press 2 for Triangule or 3 for Circumference  '))

if var == 1 :
    side =int(input('please tell the Square side:  '))
    print('the Square area is ') 
    print(measures.Square_area(side))
    print('the Square perimeter is ') 
    print(measures.Square_peri(side))
elif var == 2:
    base =int(input('please tell the Triangule Base:  '))
    height =int(input('please tell the Triangule Height:  '))
    print('the Triangule area is ') 
    print(measures.Trian_area(base,height))
elif var == 3:
    radio=int(input('please tell the circumference radio:  '))
    print('the circumference area is :  ')
    print(measures.Circunference_area(radio))
    print('the circumference Perimeter is :  ')
    print(measures.Circunference_peri(radio))
else:
    print('Wrong Selection')

   
       
   