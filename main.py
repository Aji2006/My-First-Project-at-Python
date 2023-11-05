print("----------------- Welcome To My Small Project------------------")
print("What building do you want to count? \n\n"
"Building Area of Two-Dimensional Buildings\n"
"1.  Rectangle\n"
"2.  Square\n"
"3.  Triangle\n"
"4.  Split\n"
"5.  Circle\n"
"6.  Parallelogram\n"
"7.  Trapezoid\n"
"8.  Kite\n\n"

"Volume of Three-Dimensional Buildings\n"
"9.  Beam\n"
"10. Cube\n"
"11. Cone\n"
"12. Ball\n"
"13. Triangular Prism\n"
"14. Quadrilateral Pyramid\n"
"15. Triangular Pyramid\n"
"16. Tube\n")

data_choice = input("Enter the numbers from the options above : ")
phi = 3.14 or 22/7

if data_choice == "1":
    long_side = float(input("Enter the long-side number : "))
    wide_side = float(input("Enter the wide-side number : "))
    result = long_side * wide_side
    print(f"The result of Rectangle is {result}")
elif data_choice == "2":
    wide_side = float(input("Enter the wide-side number : "))
    result = wide_side**2
    print(f"The result of Square is {result}")
elif data_choice == "3":
    tall_side = float(input("Enter the long-side number : "))
    base = float(input("Enter the base-side number : "))
    result = tall_side * base* 0.5
    print(f"The result of Triangle is {result}")
elif data_choice == "4":
    diagonal_1 = float(input("Enter the first diagonal : "))
    diagonal_2 = float(input("Enter the second diagonal : "))
    result = 0.5 * diagonal_1 * diagonal_2 
    print(f"The result of Split is {result}")
elif data_choice == "5":
    radius = float(input("Enter the radius : "))
    result = phi * radius**2
    print(f"The result of circle is {result}")
elif data_choice == "6":
    base = float(input("Enter the base-side number : "))
    tall_side = float(input("Enter the long-side number : "))
    result = base * tall_side
    print(f"The result of Parallelogram is {result}")
elif data_choice == "7": 
    a = float(input("Enter the number of a : "))
    b = float(input("Enter the number of b : "))
    t = float(input("Enter the number of t : "))
    result = 0.5 * (a+b) *t
    print(f"The result of Trapezoid is {result}")
elif data_choice == "8":
    diagonal_1 = float(input("Enter the first diagonal : "))
    diagonal_2 = float(input("Enter the second diagonal : "))
    result = 0.5 * diagonal_1 * diagonal_2 
    print(f"The result of Split is {result}")
elif data_choice == "9":
    p = float(input("Insert long side : "))
    l = float(input("Insert wide side : "))
    t = float(input("Insert high side : "))
    result = p*l*t
    print(f"The result of Beam is {result}")
elif data_choice == "10":
    s = float(input("Insert side : "))
    result = s**3
    print(f"The result of Cube is {result}")
elif data_choice == "11":
    a = float(input("Insert the base area : "))
    t = float(input("Insert high side : "))
    result = (1/3) * a * t
    print(f"The result of Cone is {result}")
elif data_choice == "12":
    r = (float(input("Insert the radius : ")))
    result = (4/3) * phi * r**3
    print(f"The result of Ball is {result}")
elif data_choice == "13":
    a = float(input("Insert the base area : "))
    t = float(input("Insert high side : "))
    result = a * t
    print(f"The result of Cone is {result}")
elif data_choice == "14" and "15":
    a = float(input("Insert the base area : "))
    t = float(input("Insert high side : "))
    result = 1/3 * a * t
    print(f"The result of Quadrilateral Pyramid or Triangular Pyramid is {result}")
elif data_choice == "16":
    r = (float(input("Insert the radius : ")))
    t = float(input("Insert high side : "))
    print(f"The result of Tube is {result}")
else: 
    print("The number you entered does not match the list")

print("Program Ended")