def check_duplicate(arr1, arr2):
    # kiem tra ngoai le
    if not arr1 or not arr2:
        return []

    d = []  # danh sach chua phan tu co o ca 2 mang
    if len(arr1) < len(arr2):
        for item in arr1:
            # phan tu co trong arr 2
            if item in arr2:
                # phan tu chua duoc cho vao danh sach
                if item not in d:
                    d.append(item)
    else:
        for item in arr2:
            if item in arr1 and item not in d:
                d.append(item)
    return d


# input:
# nhap mang 1:
len_arr1 = int(input("Do dai mang 1: "))
arr1 = []
if len_arr1 > 0:
    for i in range(len_arr1):
        item = input(f"Phan tu thu {i + 1}: ")
        if item:
            arr1.append(item)
print(f"Mang 1 la: {arr1}")


# nhap mang 2:
len_arr2 = int(input("Do dai mang 1: "))
arr2 = []
if len_arr2 > 0:
    for i in range(len_arr2):
        item = input(f"Phan tu thu {i + 1}: ")
        if item:
            arr2.append(item)
print(f"Mang 2 la: {arr2}")

# so sanh -> in ket qua
if arr1 and arr2:
    dup = check_duplicate(arr1=arr1, arr2=arr2)
    print(f"Danh sach phan tu co o ca 2 mang: {dup}")
