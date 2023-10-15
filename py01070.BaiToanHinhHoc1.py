# Hàm kiểm tra xem có tồn tại đường tròn ngoại tiếp chứa đúng K điểm hay không
def check_circle(points, k):
    n = len(points)
    
    # Duyệt qua tất cả các cặp điểm
    for i in range(n):
        for j in range(i+1, n):
            # Điểm thứ 3
            for m in range(n):
                if m != i and m != j:
                    # Tính bán kính đường tròn ngoại tiếp của 3 điểm
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[m]
                    
                    radius = ((x2-x1)**2 + (y2-y1)**2)**0.5 / 2
                    
                    # Đếm số điểm nằm trong đường tròn
                    count = 0
                    for p in range(n):
                        if p != i and p != j and p != m:
                            x, y = points[p]
                            if ((x-x1)**2 + (y-y1)**2)**0.5 <= radius:
                                count += 1
                    
                    # Kiểm tra số điểm nằm trong đường tròn có bằng K hay không
                    if count == k:
                        return "YES"
    
    return "NO"
                    

# Đọc số lượng bộ test
T = int(input())

for _ in range(T):
    # Đọc số lượng điểm và số lượng điểm cần nằm trong đường tròn
    N = int(input())
    K = int(input())
    
    points = []
    
    # Đọc tọa độ các điểm
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    
    # Kiểm tra và in kết quả
    print(check_circle(points, K))