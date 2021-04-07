

def year(n):
    if n%400==0 :
        return ("Leap Year")


    elif n%4==0 and n%100!=0:

        return ("Leap Year")

    else:

        return ("NOT Leap Year")



n = int(input("Enter which year u want 2 check:"))


i=year(n)

print(i)


