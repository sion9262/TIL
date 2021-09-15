data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]
k = 30
def solve(k, data_list):
    total_value = 0
    # [무게, 가치, 비중]
    details = []
    # 무게 / 가치가 높은 슌욿 정렬
    data_list = sorted(data_list, key=lambda x: x[1] / x[0], reverse=True)

    for data in data_list:
        if k - data[0] >= 0:
            k -= data[0]
            total_value += data[1]
            details.append((data[0], data[1], 1))
        else:
            # 남은 무게 / 넣을려는 무게  ex) 1 / 2 = 0.5 넣을 수 있음.
            count = k / data[0]
            total_value += data[1] * count
            details.append((data[0], data[1], count))
            break
    return total_value, details

print(solve(k, data_list))