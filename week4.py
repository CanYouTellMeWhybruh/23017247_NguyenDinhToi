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
                    myArray=[]
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


# Lam viec voi file

#Bai 1
def Bai1_0():
    # chon = int(input("Tạo file để ghi: 0. Đọc file: 1\n"))
    # if chon == 0:
    #     fileName = input("Nhập tên file muốn tạo: ")
    #     try:
    #         f = open(fileName, 'x')
    #         print(f"File {fileName} đã được tạo thành công.")
    #     except FileExistsError:
    #         print(f"File {fileName} đã tồn tại.")
    #     except Exception as e:
    #         print(f"Đã xảy ra lỗi: {e}")
    #     finally:
    #         if 'f' in locals():
    #             f.close()
    # elif chon == 1:
    #     file_path = input("Nhập vào tên file bạn muốn đọc: ")
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
    #         print(f"File không tồn tại: {file_path}")
    #     except Exception as e:
    #         print(f"Đã xảy ra lỗi: {e}")
    # else:
    #     print("Lựa chọn không hợp lệ. Vui lòng chọn 0 hoặc 1.")
    while True:
        try:
            file=open('test.txt')
            lines = file.readlines()
            if len(lines) < 5:
                print("file không đủ 5 dòng!")
                print(lines)
                break
            else:
                for i in range(5):
                    print(lines[i], end='')
                    break

        except:
            print("Sai cú pháp.Vui lòng nhập lại!")
    
# Gọi hàm để thực hiện
def Bai2_0():
    while True:
        try:
            print("Nhập tên file muốn tạo hoặc mở để đọc và ghi: ")
            fileName = input()
            
            with open(fileName, mode='a+', encoding='utf-8') as fileobject:
                print("Nhập nội dung bạn muốn ghi vào file:")
                toWrite = input()
                
                # Write the content to the file
                fileobject.write(toWrite)
                
                # Move the file pointer to the beginning
                fileobject.seek(0)
                
                # Read all lines from the file
                lines = fileobject.readlines()
                
                # Determine the number of lines to print
                num_lines_to_print = 5 if len(lines) >= 5 else len(lines)
                
                print("Nội dung trong file là:")
                for line in lines[-num_lines_to_print:]:
                    print(line, end='')
                
        except FileNotFoundError:
            print("Không tìm thấy file! Vui lòng thử lại.")
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}")
        
        # Ask user if they want to continue
        print("\nBạn có muốn tiếp tục không? (y/n)")
        continue_choice = input().strip().lower()
        if continue_choice != 'y':
            break









