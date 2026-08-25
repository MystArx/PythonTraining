
import package.functions as f





while True:
    choice=int(input("Enter shape :\n 1 : Circle\n 2: Triangle \n 3:Rectangle\n 4: Square \n 5: Parallelogram \n 6: Rhombus \n 7: Hexagon \n 8: Exit \n" ))
    if choice==1:
        rad=int(input("Radius :"))
        print(f"The area is {f.area_circle(rad)}. \n The circumference is {f.circumference(rad)} ")

    elif choice==2:
        side1=int(input("Enter side 1"))
        side2=int(input("Enter side 2"))
        side3=int(input("Enter side 3"))
        print(f"The area is {f.area_triangle(side1,side2,side3)}. \n The Perimeter is {f.perimeter_triangle(side1,side2,side3)} ")

    elif choice==3:
        length=int(input("Length : "))
        breadth=int(input("Breadth : "))
        print(f"The area is {f.area_rectangle(length,breadth)}. \n The Perimeter is {f.perimeter_rectangle(length,breadth)} ")

    elif choice==4:
        side=int(input("Side Length : "))
        print(f"The area is {f.area_rectangle(side,side)}. \n The Perimeter is {f.perimeter_rectangle(side,side)} ")

    elif choice==5:
        base=int(input("Base : "))
        side=int(input("Side : "))
        height=int(input("Height : "))
        print(f"The area is {f.area_parallelogram(base,height)}. \n The Perimeter is {f.perimeter_parallelogram(base,side)} ")

    elif choice==6:
        side=int(input("Side Length : "))
        theta=float(input("Angle in radians : "))
        print(f"The area is {f.area_rhombus(side,theta)}. \n The Perimeter is {f.perimeter_rhombus(side)} ")

    elif choice==7:
        side=int(input("Side Length : "))
        print(f"The area is {f.area_hexagon(side)}. \n The Perimeter is {f.perimeter_hexagon(side)} ")

    elif choice==8:
        print("Exiting")
        break

    else:
        print("Enter valid input!")
    





