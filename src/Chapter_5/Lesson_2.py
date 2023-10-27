#DICTIONARY
## Thêm và cập nhật phân tử
### Tạo một dictionary chứa thông tin học viên
danh_sach_hoc_vien={}
### Thêm thông tin của học viên vào Dictionary
danh_sach_hoc_vien['hv0001']={
    'ho_ten':'Trần Thanh Phong',
    'tuoi': 25,
    'lop':'Nâng cao'
}
danh_sach_hoc_vien['hv0002']={
    'ho_ten':'Trần Thanh Long',
    'tuoi': 24,
    'lop':'Nâng cao'
}
danh_sach_hoc_vien['hv0003']={
    'ho_ten':'Trần Thanh Nam',
    'tuoi': 25,
    'lop':'Cơ bản'
}
danh_sach_hoc_vien['hv0004']={
    'ho_ten':'',
    'tuoi': 0,
    'lop':''
}
print(danh_sach_hoc_vien)

#### In thông tin trươc khi thay đổi
# print(danh_sach_hoc_vien['hv0001'])
# danh_sach_hoc_vien['hv0001']['tuoi'] = 24
#### In thông tin sau khi thay đổi
# print(danh_sach_hoc_vien['hv0001'])

## Xóa phân tử
### In danh sách trước khi xóa
# print(danh_sach_hoc_vien)

# del danh_sach_hoc_vien['hv0001']

### In danh sách sau khi xóa
# print(danh_sach_hoc_vien)

### In số lượng học viên tức là số cặp key-value của danh_sach_hoc_vien
# print(len(danh_sach_hoc_vien))

### In số lượng cặp key-value của học viên có mã hv0001
# print(len(danh_sach_hoc_vien['hv0002']))

## Lấy danh sách các keys của Dic
# print(danh_sach_hoc_vien.keys())

## Để chuyển dict_keys thành list dùng hàm list(dict_keys)
# print(list(danh_sach_hoc_vien.keys()))

## In danh sách gia trị của danh_sach_hoc_vien['hv0001']
# print(list(danh_sach_hoc_vien['hv0001'].values()))

## Kiểm tra một key có tồn tại hay không
# if 'hv0001' in danh_sach_hoc_vien:
#     print('Mã hv0001 có trong danh sách')
# else:
#     print('Mã hv0001 không có trong danh sách')
## Tạo bản sao của học viên mã hv0001 lưu vào mã hv0004
# danh_sach_hoc_vien['hv0004'] = danh_sach_hoc_vien['hv0001'].copy()
# print(danh_sach_hoc_vien['hv0004'])

# Xóa toàn bộ dữ liệu của dict
print(danh_sach_hoc_vien['hv0001'].clear())
