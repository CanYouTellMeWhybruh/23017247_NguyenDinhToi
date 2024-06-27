from math import *

#Bai 1 Viet ham average
def average():
    print("Vui long nhap lan luot 5 gia tri nguyen:")
    a,b,c,d,e=map(int,input().split())
    average=(a+b+c+d+e)/5
    print("Gia tri trung binh cua 5 gia tri la {:.2f}".format(average))
#Bai 2 Viet ham area
def area():
    print("Vui long nhap do dai cua ba canh tam giac:")
    a,b,c=map(float,input().split())
    p=(a+b+c)/2
    S=(p*(p-a)*(p-b)*(p-c))**(1/2)
    print("Dien tich cua tam giac la {:.2f}".format(S))
#Bai 3 Viet ham area2
def area2():
    print("Vui long nhap toa do theo mau : x1,y1,x2,y2,x3,y3")
    x1,y1,x2,y2,x3,y3=map(int,input().split())
    S= (1/2) * abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3))
    print("Dien tich tam giac la {:.2f}".format(S))
#Bai 4 Viet ham total
def total():
    print("Nhap mot gia tri nguyen:")
    n=int(input())
    total=0
    while(n>0):
        total+=(n%10)
        n//=10
    print(f'Tong cac chu so cua n la {total}')
# Bai 5 Viet ham isFIbo
def checkfibo():
    def is_perfect_square(x):
        s = int(sqrt(x))
        return s * s == x
    def is_fibonacci(n):
        return is_perfect_square(5*(n**2) + 4) or is_perfect_square(5*(n**2) - 4)
    num = int(input("Nhap vao mot so nguyen: "))
    if is_fibonacci(num):
        print(f"{num} la mot so fibonacci.")
    else:
        print(f"{num} khong phai so fibonacci.")
# Bai 6 Tinh tong giai thua
def gt():
    print("Nhap vao mot so nguyen:")
    def gt2(gg):
        total2=1
        for i in range(1,gg+1):
            total2*=i
        return total2
    n=int(input())
    total=0
    if (n>0):
        for i in range(1,n+1):
            total+=gt2(i)
        print(f'Tong giai thua la {total}')
    else:
        print("n khong the am")
#Bai 7 Chuong trinh danh gia hoc sinh
def rate():
    print("Nhap diem cua hoc sinh:")
    diem=float(input())
    if(diem<3.5):
        print("Yeu")
    elif(diem>=3.5 and diem<5):
        print("Kem")
    elif(diem>=5 and diem <6.5):
        print("Trung Binh")
    elif(diem>=6.5 and diem < 8):
        print("Kha")
    elif(diem >= 8 and diem < 9):
        print("Gioi")
    else:
        print("Xuat Sac")
#Bai 8 Tim so lon nhat
def max():
    print("Nhap vao ba so:")
    a,b,c=map(int,input().split())
    if(a>b and a>c):
        print(f'{a} la so lon nhat')
    elif(b>a and b>c):
        print(f'{b} la so lon nhat')
    elif(c>a and c>b):
        print(f'{c} la so lon nhat')
    elif(a==b):
        print(f'{c}')
    elif(a==c):
        print(f'{b}')
    else:
        print(f'{a}')
#Bai 9 Hien thi ngay tiep theo
def predict():
    print("Nhap lan luot ngay thang nam:")
    a,b,c=map(int,input().split())
    if((c%4 == 0 and c%100 != 0) or c%400 == 0):
        if (b==2):
            if (a>29):
                print("Khong co ngay nay trong thang nay")
            elif (a==29):
                a=1
                b=3
                print(f'Ngay tiep theo la ngay {a} thang {b} nam {c} ')
            else:
                a+=1
                print(f'Ngay tiep theo la ngay {a} thang {b} nam {c}')
        elif( b==4 or b==6 or b==9 or b==11):
            if (a>30):
                print("Khong co ngay nay trong thang nay")
            elif(a==30):
                a=1
                b+=1
                print(f'Ngay tiep theo se la ngay {a} thang {b} nam {c}')
            else:
                a+=1
                print(f'Ngay tiep theo se la ngay {a} thang {b} nam {c}')
        elif(b==12):
            if(a>31):
                print("Khong co ngay nay trong thang nay")
            elif(a==31):
                a=1
                b=1
                c+=1
                print(f'Ngay tiep theo se la ngay {a} thang {b} nam {c}')
            else:
                a+=1
                print(f'Ngay tiep theo se la ngay {a} thang {b} nam {c}')
        else:
            if(a>30):
                print("Khong co ngay nay trong thang nay")
            elif(a==30):
                a=1
                b+=1
                print(f'Ngay tiep theo se la ngay {a} thang {b} nam {c}')
            else:
                a+=1
                print(f'Ngay tiep theo se la ngay {a} thang {b} nam {c}')
    else:
        if (b==2):
            if (a>28):
                print("Khong co ngay nay trong thang nay")
            elif (a==28):
                a=1
                b=3
                print(f'Ngay tiep theo la ngay {a} thang {b} nam {c} ')
            else:
                a+=1
                print(f'Ngay tiep theo la ngay {a} thang {b} nam {c}')
        elif( b==4 or b==6 or b==9 or b==11):
            if (a>30):
                print("Khong co ngay nay trong thang nay")
            elif(a==30):
                a=1
                b+=1
                print(f'Ngay tiep theo se la ngay {a} thang {b} nam {c}')
            else:
                a+=1
                print(f'Ngay tiep theo se la ngay {a} thang {b} nam {c}')
        elif(b==12):
            if(a>31):
                print("Khong co ngay nay trong thang nay")
            elif(a==31):
                a=1
                b=1
                c+=1
                print(f'Ngay tiep theo se la ngay {a} thang {b} nam {c}')
            else:
                a+=1
                print(f'Ngay tiep theo se la ngay {a} thang {b} nam {c}')
        else:
            if(a>31):
                print("Khong co ngay nay trong thang nay")
            elif(a==31):
                a=1
                b+=1
                print(f'Ngay tiep theo se la ngay {a} thang {b} nam {c}')
            else:
                a+=1
                print(f'Ngay tiep theo se la ngay {a} thang {b} nam {c}')
n='2 3 4 5 6 7'
n=n.split()
lt=[]
lt.append(n)
print(lt)

            
