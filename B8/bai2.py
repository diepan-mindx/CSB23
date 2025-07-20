# O(n^2)
import glob


def insertion_sort(arr):
    # duyet qua tung phan tu -> tim vi tri nho nhat
    for index in range(1, len(arr)):
        insert_index = index
        current_value = arr.pop(index)  # xoa phan tu tai index
        for j in range(index - 1, -1, -1):
            if arr[j] > current_value:
                insert_index = j
        arr.insert(insert_index, current_value)  # them lai phan tu vao vi tri moi
    return arr


# bien toan cuc
color_code = {"r": 1, "w": 2, "b": 3}

def convert_color_code(color_arr):
    global color_code
    # chuyen danh sach mau sac -> chu
    result = []
    for c in color_arr:
        num = color_code[c]
        result.append(num)
    # check ngoai le -> danh sach ghi khong dung ten mau
    if len(result) != len(color_arr):
        raise ValueError("Danh sách chứa tên màu không đúng quy định (r,w, b)")
    return result


def convert_color_char(color_num):
    global color_code
    result = []
    for num in color_num:
        for key, value in color_code.items():
            if value == num:
                result.append(key)
    # mgoai le
    if len(result) != len(color_num):
        raise ValueError("Danh sách chứa mã màu không đúng quy định (1,2,3)")
    return result


def test_drive():
    print("Start----------------------")
    # nhap ham vao
    color_arr = input("Nhap danh sach (r, w, b), moi phan tu cach nhau 1 space:\n")
    try:
        # cat chuoi -> list
        color_arr = color_arr.split(" ")
        # convert color code
        color_code_list = convert_color_code(color_arr)
        # sap xep
        sorted_color_code_list = insertion_sort(color_code_list)
        # convert color code
        sorted_color_char_list = convert_color_char(sorted_color_code_list)
        # print
        print(sorted_color_char_list)
    except Exception as e:
        print("Error: ", e)
    finally:
        print("End----------------------")


test_drive()
