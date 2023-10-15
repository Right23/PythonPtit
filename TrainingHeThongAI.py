import math

# Hàm tính độ chính xác lớn nhất sau khi training
def max_accuracy(N, U, P):
    max_accuracy = 1.0
    
    # Duyệt qua từng module
    for i in range(N):
        # Tính thời gian training cho module i
        training_time = min(U, 1.0 - P[i])
        
        # Cập nhật độ chính xác lớn nhất
        max_accuracy *= (P[i] + training_time)
        
        # Giảm thời gian training đã sử dụng
        U -= training_time
    
    return max_accuracy

# Đọc số bộ test
T = int(input())

for _ in range(T):
    # Đọc số lượng module và thời gian training
    N = int(input())
    U = float(input())
    
    # Đọc độ chính xác của từng module
    P = list(map(float, input().split()))
    
    # Tính và in ra độ chính xác lớn nhất
    result = max_accuracy(N, U, P)
    print("{:.6f}".format(result))