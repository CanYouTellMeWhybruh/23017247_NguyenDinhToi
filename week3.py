from math import *
#Phan 8: Frozenset

#Bai 1
def Bai1_2():
    lt=[x for x in range(100)]
    print(lt)
#Bai 2
def Bai2_2():
    lt=[x for x in range(1,200) if x%2 != 0 ]
    print(lt)
#Bai 3
def Bai3_2():
    n = input("Nhập một dãy số cách nhau bởi dấu cách: ")
    n = n.split()
    n = set(n)  # Remove duplicates
    n = list(map(int, n))  # Convert to integers
    
    if len(n) == 0:
        print("Không có số nào được nhập.")
        return
    
    max_in_list = n[0]
    min_in_list = n[0]
    
    for i in n:
        if i > max_in_list:
            max_in_list = i
        if i < min_in_list:
            min_in_list = i
    
    print("Tập số mà bạn vừa nhập là {}".format(n))
    print("Số lớn nhất trong tập là {} và nhỏ nhất trong tập là {}".format(max_in_list, min_in_list))
#Bai 4
def Bai4_2():
    lt=[]
    i=1
    while(1):
        print("Nhap ten cua sinh vien thu {}".format(i))
        n=input()
        if(len(n)==0):
            break
        lt.append(n)
        i+=1
    for i in range(len(lt)):
        print("Ho va ten ban sinh vien thu {} la : {}".format(i+1,lt[i]))
#Bai 5
def UC():  
    print("Nhap so nguyen n:")
    n=int(input())
    Uc=[]
    for i in range(1,n+1):
        if(n%i==0):
            Uc.append(i)
    print(Uc)
#Bai 6
def Usc():
    print('Nhap 2 so nguyen a va b:')
    a,b=map(int,input().split())
    Uc=[]
    for i in range(1,int(sqrt(a*b))+1):
        if(a%i==0 and b%i==0):
            Uc.append(i)
    print(Uc)
#Bai 7
def Bai7():
    n=input("Nhap mot day so nguyen ngan cach boi dau cham phay: ")
    n=n.split(';')
    n=set(n)
    n=list(n)
    print("Day cua ban sau khi xoa bo nhung so giong nhau la: {}".format(n))
    print("Day co {} so khac nhau.".format(len(n)))
#Bai 8
def Bai8():
    i = 1
    lt = []
    while True:
        print("Nhap 6 so cua nguoi thu {} (luu y moi so cach nhau boi dau cach) : ".format(i))
        n = input()
        n = n.split()
        if len(n) == 0 or len(n) < 6:
            break
        else:
            lt.append([int(x) for x in n])
        i += 1
    
    n = input('Nhap vao nhung so trong giai dac biet (co 6 so tu 1-45): ')
    n = n.split()
    special_numbers = [int(x) for x in n]
    
    lt2 = []
    
    for user_numbers in lt:
        count = 0
        for number in user_numbers:
            if number in special_numbers:
                count += 1
        if count >= 5:
            lt2.append(user_numbers)
    
    print("Nhung nguoi da trung giai dac biet la: {}".format(lt2))

Bai8()

    