def tao_tuple_tu_list(lst):

    return tuple(lst)
input_list = input ("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
# Tạo tuple và in kết quả
my_tuple = tao_tuple_tu_list (numbers)
print("List: ", numbers)
print ("Tuple tù List:", my_tuple)