from math import *
#Phan 2 Vong lap for
#Bai 1
def is_prime():
    n=int(input("Nhap vao so can kiem tra: "))
    k=sqrt(n)
    b=True
    if(n<2):
        print('So nguyen to khong the nho hon 2!')
    else:   
        for i in range(2,int(k+1)):
            if(n%i==0):
                print(f'{n} khong phai la so nguyen to')
                b=False
                break
            elif(n==2):
                break
        if(b):
            print(f'{n} la so nguyen to')
#Bai 2
def ab():
    def kt(n):
        k=sqrt(n)
        b=True
        if(n<2):
            return False
        else:   
            for i in range(2,int(k+1)):
                if(n%i==0):
                    b=False
                    break
                elif(n==2):
                    break
            if(b):
                return True
            else:
                return False
    mang=[]
    print("Nhap vao khoang a b:")
    a,b = map(int,input().split())
    for i in range(a,b+1,1):
        if (kt(i)):
            mang.append(i)
        else:
            continue
    print(mang)
#Bai 3
def Chung():
    print("Nhap vao 2 so nguyen duong a va b:")
    a,b=map(int, input().split())
    def kt(a,b):
        while (b!=0):
            a,b=b,a%b
        else:
            print(f'{a} la uoc chung lon nhat cua hai so a va b')
    kt(a,b)
    for i in range(1,50000):
        if(i%a==0 and i%b==0):
            print(f'{i} la boi chung nho nhat cua a va b')
            break        
#Bai 4
def kt(a,b):
        while (b!=0):
            a,b=b,a%b
        else:
            return a
def lcm(a, b):
    return abs(a * b) // kt(a, b)
def Chung2():
    listt = []
    while True:
        a = int(input("Nhap vao so ban muon: "))
        if a <= 0:
            break
        else:
            listt.append(a)
    
    if len(listt) < 2:
        print("Nhap it nhat hai so")
        return
    
    gg = kt(listt[0], listt[1])
    gg2=lcm(listt[0],listt[1])
    for i in range(2, len(listt)):
        gg = kt(gg, listt[i])
        gg2 = lcm(gg2,listt[i])
    print(f'{gg} la uoc chung lon nhat trong mang')
    print(f'{gg2} la boi chung nho nhat trong mang')
#Bai 5
def findmax(current_max, n):
    if n > current_max:
        return n
    else:
        return current_max

def findmin(current_min, n):
    if n < current_min:
        return n
    else:
        return current_min

def idk():
    listt = []
    while True:
        a = int(input("Nhap vao so ban muon: "))
        if a == 0:
            del listt[len(listt) -1] 
            break
        else:
            listt.append(a)
    
    if not listt: 
        print("Danh sach rong")
        return

    max_value = listt[0]
    min_value = listt[0]

    for num in listt:
        max_value = findmax(max_value, num)
        min_value = findmin(min_value, num)
    
    print(f'{max_value} la gia tri lon nhat trong mang')
    print(f'{min_value} la gia tri nho nhat trong mang')
#Bai tap ve xu li chuoi
#Bai 1
def nhap_chuoi():
    chuoi = input("Nhap vao mot chuoi: ")
    if len(chuoi) < 3:
        print("Chuoi qua ngan de thay the ky tu!")
        return

# Chuyển chuỗi thành danh sách để có thể thay đổi
    chuoi_list = list(chuoi)
    for i in range(len(chuoi) - 3, len(chuoi)):
        chuoi_list[i] = '!'

# Chuyển danh sách trở lại thành chuỗi
    chuoi_moi = ''.join(chuoi_list)
    print(f'Chuoi ban vua nhap la: "{chuoi_moi}"')

#Bai 2
def nhapso():
    day_so=input("Nhap vao mot day so cach nhau boi dau cach:")
    listt=day_so.split()
    for num in listt:
        int(num)
    print(f'Day so ban vua nhap la {listt}')
#Bai 3
def nhap_ten():
    ten = input("Nhap vao ten cua ban: ")
    print(f'Ten ban vua nhap la: "{ten}"')
    ten=ten.split()
    ho=ten[0]+' '+ten[1]
    ten2=ten[2]
    print('Ho cua ban la : {}'.format(ho))
    print("Ten cua ban la: {}".format(ten2))
#Bai 4
def nhapchuoi():
    gg = input("Nhap vao chuoi cua ban: ")
    chuoi = list(gg)
    chuoi_moi = ''
    for chu in chuoi:
        if not chu.isdigit():
            chuoi_moi += chu
    print(f'Chuoi ban vua nhap la: {chuoi_moi}')
#Bai Vd
def N():
    n=int(input("Nhap chieu cao:"))
    for i in range(n):
        for j in range(n):
            if j == 0 or j==i or j==n-1:
                print("*",end='')
            else: 
                print(" ",end='')
        print()
#Bai 5
# d=';'.join(('1', '2', '3'))
# print(d)
def longest():
    print("Nhap vao mot day cac tu va ngan cach nhau boi dau cach:")
    n=input()
    n=n.split()
    b=''
    for i in range(len(n)):
        if len(n[i]) > len(b):
            b=n[i]
        else:
            continue
    n.remove(b)
    for i in range(len(n)):
        if len(n[i]) == len(b):
            b = b + ' ' + n[i]
            n.remove(n[i])
    print(f'Nhung tu dai nhat trong mang la: {b}')
#Bai 6
def count():
    print("Nhap vao mot day cac tu va ngan cach nhau boi dau cach:")
    n=input()
    g=n.replace(" ",'')
    d=set(g)
    char_count = {}
    for char in g:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char] = 1
    print("Nhung chu cai xuat hien la: {}".format(d))
    for char, count in char_count.items():
        print(f"Chu '{char}' xuat hien {count} lan ")
#Bai 7
def find_max2():
    print("Nhập vào một chuỗi các ký tự là chữ số:")
    n = input()
    print("Nhập vào số lượng chữ số bạn muốn xóa:")
    m = int(input())

    stack = []
    to_remove = m

    for digit in n:
        while to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)
    final_stack = stack[:-to_remove] if to_remove else stack

    max_number = ''.join(final_stack)
    print(f'Số lớn nhất mà ta nhận được sau khi xóa {m} ký tự là {max_number}')
#Bai 8
def rpl():
    n = input("Nhập vào một chuỗi: ")
    chuoi = ''
    for char in n:
        if char.isdigit():
            chuoi += '?'  
        else:
            chuoi += char  
    print(chuoi)
#Phan 6: Range
# list comprehension : Bo suy dien danh sach 
# X = [[x,(x**2)] for x in range(50)]
# print(X)
#Bai 1
def Bai1():
    n=input("Nhap vao cac tu tieng anh cach nhau boi dau cach:")
    m=n.replace(" ",'')
    m=set(m)
    b =''.join(m)
    sorted_list=sorted(b)
    sorted_string=''.join(sorted_list)
    sorted_string=list(sorted_string)
    print(sorted_string)
#Bai 2
def Bai2():
    n=input("Nhap tu ban phim chuoi so nhi phan ngan cach boi dau cham phay:")
    n=n.split(';')
    lt1=[]
    total=0
    for i in range(len(n)):
        for j in range(len(n[i])):
            total+=int(n[i][j])*(2**j)
        lt1.append(total)
        total=0
    print("Nhi phan chuyen sang so thap phan la: {}".format(lt1))
#Bai 3
def Bai3():
    n=int(input("Nhap so nguyen duong n:"))
    lt1=[]
    total=0
    for i in range(1,n):
        for j in range(1,i):
            if i%j==0:
                total+=j
        if total > i:
            lt1.append(i)
    if lt1 == []:
        print("Khong co so nao nho hon n ma có tổng ước lớn hơn nó!")
    else:
        print('Tập hợp những số nguyên dương nhỏ hơn {} và có tổng các ước số lớn hơn chính nó là:'.format(n))
        print(lt1)
#Bai 4
import re
def Bai4():
    def is_valid_email(email):
        # Định nghĩa biểu thức chính quy cho email hợp lệ
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        # Sử dụng re.match để kiểm tra email
        if re.match(regex, email):
            return True
        else:
            return False
    emails = input("Nhập email mà bạn muốn: ")
    print(f"{emails}: {'Hợp lệ' if is_valid_email(emails) else 'Không hợp lệ'}")
#Bai 5
# # In ra n dòng tam giác pascal
# n=int(input("Nhap chieu cao cua thap:"))
# l=n-1
# g=1
# lt=[1]
# lt2=[1,1]
# for i in range(n):
#     for j in range(l):
#         print(" ",end='')
#     l-=1
#     for j in range(1,g+1):
#         if j%2==0:
#             print(" ",end='')
#         else:
#             for i in range(n):
#                 for j in range(i):
#                     if j > 0 and j < i-1:
#                         lt2.append(lt[j-1]+lt[j])
#                     else:

#                 lt=lt2
#                 lt2=[]

#     g+=2
#     print()
def pascalTriangle():
    n = int(input("Nhap chieu cao cua thap:"))
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    width = len("   ".join(map(str, triangle[-1])))
    for row in triangle:
        row_str = "   ".join(map(str, row))
        print(row_str.center(width))
#Bai 6
def checkfibo():
    def is_perfect_square(x):
        s = int(sqrt(x))
        return s * s == x
    def is_fibonacci(n):
        return is_perfect_square(5*(n**2) + 4) or is_perfect_square(5*(n**2) - 4)
    lt=[]
    n=int(input("Nhap vao so n:"))
    for i in range(n):
        if is_fibonacci(i):
           lt.append(i)
    print("Những số fibonachi nhỏ hơn n là {}".format(lt))
#Bai 7
def nt(n):
    for i in range(2,int(sqrt(n)) + 1):
        if (n%i == 0):
            return False 
        else:
            return True
def Bai7():
    n=int(input("Nhap giới hạn mà bạn muốn kiểm tra số nguyên tố:"))
    lt=[]
    for i in range(n):
        if(nt(i)):
            lt.append(i)
        else:
            continue
    print("Những số nguyên tố nhỏ hơn {} là {}".format(n,lt))

pascalTriangle()




        


            

        

            
                
                    

            