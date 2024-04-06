from datetime import datetime

def elapsed_time(start_time):
    end_time = datetime.now()
    elapsed = end_time - start_time
    return elapsed
    
def knapsack(items, hand_limit):
    # 아이템의 개수와 손에 들 수 있는 최대 무게
    n = len(items)
    dp = [[0] * (hand_limit + 1) for _ in range(n + 1)]

    # 다이나믹 프로그래밍을 통해 최적의 가치를 계산
    for i in range(1, n + 1):
        for w in range(1, hand_limit + 1):
            weight, value = items[i - 1][1], items[i - 1][2]
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]

    # 최적의 가치를 찾기 위해 역추적
    total_value = dp[n][hand_limit]
    total_weight = hand_limit
    stolen_items = []
    for i in range(n, 0, -1):
        if dp[i][total_weight] != dp[i - 1][total_weight]:
            item_name = items[i - 1][0]
            stolen_items.append(item_name)
            total_weight -= items[i - 1][1]

    return stolen_items, total_value

start_time = datetime.now()

# 물건 종류, 무게, 가치
items = [
    ('컴퓨터 알고리즘 책', 1, 500),
    ('노트북', 10, 2000),
    ('아이패드', 5, 1500),
    ('아이폰', 3, 1000)
]

# 손에 들 수 있는 무게
hand_limit = 10

stolen_items, total_value = knapsack(items, hand_limit)
print("훔친 물건:", stolen_items)
print("총 훔친 물건의 가치:", total_value)
    
end_time = datetime.now()
elapsed = elapsed_time(start_time)    
print("코드가 실행되는데 걸린 시간:", elapsed)
