def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # 每次迭代會將最大的數推到最後
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # 交換元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 測試氣泡排序
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("原始數組:", data)
    sorted_data = bubble_sort(data)
    print("排序後數組:", sorted_data)