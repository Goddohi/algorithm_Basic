# 과제 종류, 걸리는 시간, 마감 시간, 학점
assignments = [
    ('취창업 실무 과제', 1, 14, 3.0),
    ('컴퓨터 알고리즘 과제', 1, 13, 4.5),
    ('인공지능 캡스톤 과제', 1, 14, 3.5),
    ('빅데이터 활용 과제', 1, 13, 4.0)
]

# 현재 시간
current_time = 12

# 마감 시간까지의 시간을 고려하여 학점을 최대화하는 순서 결정
sorted_assignments = sorted(assignments, key=lambda x: (-x[3], x[2]))  # 학점이 높은 순서로 정렬, 마감 시간이 빠른 순으로 정렬

total_time = 0
total_reward=0
count =0
optimal_order = []

for assignment in sorted_assignments:
    if current_time + total_time + assignment[1] <= assignment[2]:  # 마감 시간 이내에 과제를 마칠 수 있는지 확인
        total_time += assignment[1]
        total_reward += assignment[3]
        optimal_order.append(assignment[0])
        count+=1

print("가장 효율적인 순서:", optimal_order)
print("학점 총 보상:", total_reward/count)
