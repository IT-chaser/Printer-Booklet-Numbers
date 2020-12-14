a = int(input("Enter Starting page number: "))
b = int(input("Enter Ending page number: "))
c = (b + 1) - a
if c % 4 == 0:
    b1 = b
    a1 = a
    numbers = [b1, a1]
    while (b1-a1) != 3:
        b1=b1-2 
        a1=a1+2
        numbers.append(b1)
        numbers.append(a1)
    print(f" First Half: {numbers}")
    b2 = b-1
    a2 = a+1
    numbers2 = [b2, a2]
    while (b2-a2) != 1:
        a2 = a2 + 2
        b2 = b2 - 2
        numbers2.append(b2)
        numbers2.append(a2)
    numbers2.reverse()
    print(f"Second Half: {numbers2}")
else:
    while c % 4 !=0:
        b +=1
        c = (b + 1) - a
        if c % 4 == 0:
            b1 = b
            a1 = a
            numbers = [b1, a1]
            while (b1-a1) != 3:
                b1=b1-2 
                a1=a1+2
                numbers.append(b1)
                numbers.append(a1)
            print(f"First Half: {numbers}")
            b2 = b-1
            a2 = a+1
            numbers2 = [b2, a2]
            while (b2-a2) != 1:
                a2 = a2 + 2
                b2 = b2 - 2
                numbers2.append(b2)
                numbers2.append(a2)
                
            numbers2.reverse()
            print(f"Second Half: {numbers2}")
