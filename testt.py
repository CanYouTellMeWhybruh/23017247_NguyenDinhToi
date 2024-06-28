with open('test.txt', mode='r', encoding='utf-8') as fileobject:
    print(fileobject.read())
import os

# file_path = 'test.txt'

# # In thông tin chi tiết về file và thư mục
# print(f"Đường dẫn hiện tại: {os.getcwd()}")
# print(f"Đường dẫn đầy đủ đến file: {os.path.abspath(file_path)}")

# # Kiểm tra file
# if os.path.exists(file_path):
#     print("File tồn tại.")
#     if os.access(file_path, os.R_OK):
#         print("Có quyền đọc file.")
#     else:
#         print("Không có quyền đọc file.")
# else:
#     print("File không tồn tại.")


