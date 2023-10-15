# Hàm xoay xâu ký tự
def rotate_string(s):
    # Tính tổng giá trị xoay của xâu
    rotation_value = sum(ord(c) - ord('A') for c in s)
    
    # Xoay xâu
    rotated_string = ""
    for c in s:
        rotated_char = chr((ord(c) - ord('A') + rotation_value) % 26 + ord('A'))
        rotated_string += rotated_char
    
    return rotated_string


# Hàm trộn hai xâu ký tự
def merge_strings(s1, s2):
    merged_string = ""
    for c1, c2 in zip(s1, s2):
        merge_char = chr((ord(c1) - ord('A') + ord(c2) - ord('A')) % 26 + ord('A'))
        merged_string += merge_char
    
    return merged_string


# Đọc số bộ test
T = int(input())

for _ in range(T):
    # Đọc xâu ký tự cần mã hóa
    s = input()
    
    # Thực hiện bước chia
    half = len(s) // 2
    s1 = s[:half]
    s2 = s[half:]
    
    # Thực hiện bước xoay
    rotated_s1 = rotate_string(s1)
    rotated_s2 = rotate_string(s2)
    
    # Thực hiện bước trộn
    encoded_string = merge_strings(rotated_s1, rotated_s2)
    
    # In kết quả
    print(encoded_string)