# 과제 종류와 걸리는 시간
assignments = {
    '취창업 실무 과제': 3,
    '컴퓨터 알고리즘 과제': 5,
    '인공지능 캡스톤 과제': 2
}

# 걸리는 시간이 짧은 순서로 정렬
sorted_assignments = sorted(assignments.items(), key=lambda x: x[1])

# 가장 효율적인 순서와 소요 시간 계산
play_time = 0
system_time=0
optimal_order = []
for assignment, time in sorted_assignments:
    optimal_order.append(assignment)
    system_time+= play_time
    play_time += time
    
    
total_time = system_time+play_time
    
print("가장 효율적인 순서:", optimal_order)
print("소요 시간:", total_time, "시간")
