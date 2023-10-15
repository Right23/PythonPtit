# Hàm tính diện tích toàn phần của khối thể tích
def calculate_surface_area(heights, M, N):
    total_area = 0
    
    # Tính diện tích mặt đáy
    bottom_area = M * N
    total_area += bottom_area
    
    # Tính diện tích mặt trên
    top_area = M * N
    total_area += top_area
    
    # Tính diện tích các mặt xung quanh
    for i in range(M):
        for j in range(N):
            # Tính diện tích mặt phía trước và phía sau
            if i == 0:
                front_area = heights[i][j]
            else:
                front_area = max(0, heights[i][j] - heights[i-1][j])
            total_area += front_area
            
            if i == M - 1:
                back_area = heights[i][j]
            else:
                back_area = max(0, heights[i][j] - heights[i+1][j])
            total_area += back_area
            
            # Tính diện tích mặt phía trái và phía phải
            if j == 0:
                left_area = heights[i][j]
            else:
                left_area = max(0, heights[i][j] - heights[i][j-1])
            total_area += left_area
            
            if j == N - 1:
                right_area = heights[i][j]
            else:
                right_area = max(0, heights[i][j] - heights[i][j+1])
            total_area += right_area
    
    return total_area

# Đọc số lượng bộ test
T = int(input())

# Vòng lặp qua từng bộ test
for _ in range(T):
    # Đọc kích thước M và N
    M, N = map(int, input().split())
    
    # Khởi tạo ma trận chiều cao
    heights = []
    for _ in range(M):
        row = list(map(int, input().split()))
        heights.append(row)
    
    # Tính và in ra diện tích toàn phần
    result = calculate_surface_area(heights, M, N)
    print(result)