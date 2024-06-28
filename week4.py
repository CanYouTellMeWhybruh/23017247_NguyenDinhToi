from math import *
# def print_first_five_lines(file_path):
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             lines = file.readlines()
#             if len(lines) < 5:
#                 for line in lines:
#                     print(line, end='')
#             else:
#                 for i in range(5):
#                     print(lines[i], end='')
#     except FileNotFoundError:
#         print(f"File not found: {file_path}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Ví dụ sử dụng:
# file_path = 'duong_dan_den_file_cua_ban.txt'
# print_first_five_lines(file_path)




# while True:
#     try: 
#         x=int(input("Nhap so X: "))
#         break
#     except ValueError:
#         print("Lỗi, hãy nhập lại.")
# print("X = ",x)





# Bai 1
def Bai1():
    while True:
        try:
            a=int(input("Nhap vao so a: "))
            b=int(input("Nhap vao so b: "))
            print("A CHIA B = {:.2f}".format(a/b))
            break
        except:
            print("a và b nhập không hợp lệ vui lòng nhập lại!")


#Bai 2

def Bai2():
    while True:
        try:
            a, b, c = map(int, input("Nhập ba số nguyên dương a, b, c: ").split())
            if (a + b > c) and (a + c > b) and (b + c > a):
                print("Độ dài ba cạnh của tam giác lần lượt là {}, {}, {}".format(a, b, c))
                break
            else:
                print("Ba cạnh a, b, c không thể tạo thành một tam giác. Vui lòng nhập lại.")
                continue
        except ValueError:
            print("a hoặc b hoặc c không hợp lệ! Vui lòng nhập lại.")
myArray=[]
# def findnum(n):
#     tempArray=[]
#     for i in (len(myArray)):
#         if n==myArray[i]:
#             tempArray.append(i)
            

#Bai 3
def Bai3():
    while True:
        try:
            myArray = []
            
            while True:
                n = int(input("Nhập số nguyên dương vào dãy (nhập 0 để kết thúc): "))
                if n == 0:
                    break
                elif n < 0:
                    print("Lỗi số âm!")
                    continue
                myArray.append(n)
                
                if len(myArray) >= 4:
                    # Check the last 4 elements to see if they are all the same(Tự dịch)
                    if myArray[-1] == myArray[-2] == myArray[-3] == myArray[-4]:
                        print("Người dùng đã nhập vào 4 số giống nhau liên tiếp. Mời nhập lại!")
                        myArray=[]
                        continue
                
                if len(myArray) >= 5:
                    # Check the last 5 elements to see if they are all even(Tự dịch)
                    if (myArray[-1] % 2 == 0 and myArray[-2] % 2 == 0 and 
                        myArray[-3] % 2 == 0 and myArray[-4] % 2 == 0 and 
                        myArray[-5] % 2 == 0):
                        print('Người dùng đã nhập vào 5 số chẵn liên tiếp. Mời nhập lại!')
                        myArray=[]
                        continue
            
            # Convert to a set to remove duplicates and print the set(Tự dịch)
            mySet = set(myArray)
            print("Dãy số không trùng lặp:", mySet)
            break
        
        except ValueError:
            print("Lỗi nhập số! Vui lòng nhập một số nguyên.")

Bai3()




