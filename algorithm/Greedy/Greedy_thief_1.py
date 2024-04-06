from datetime import datetime

def elapsed_time(start_time):
    end_time = datetime.now()
    elapsed = end_time - start_time
    return elapsed
    
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

# 가방에 넣을 수 있는 가장 비싼 물건을 선택하는 탐욕 알고리즘
items.sort(key=lambda x: x[2], reverse=True)  # 물건을 가치순으로 정렬

total_weight = 0
total_value = 0
stolen_items = []

for item in items:
    if total_weight + item[1] <= hand_limit:  # 아직 손에 들 수 있는 무게가 남아있는 경우
        total_weight += item[1]
        total_value += item[2]
        stolen_items.append(item[0])

print("훔친 물건:", stolen_items)
print("총 훔친 물건의 가치:", total_value)
    
end_time = datetime.now()
elapsed = elapsed_time(start_time)    
print("코드가 실행되는데 걸린 시간:", elapsed)
