from datetime import datetime

def elapsed_time(start_time):
    end_time = datetime.now()
    elapsed = end_time - start_time
    return elapsed

start_time = datetime.now()

change = 100000
bills = [70000, 50000, 10000, 5000, 1000]

counts = []
for bill in bills:
    count = change // bill
    counts.append(count)
    change -= bill * count

total_bills = sum(counts)
print("각 지폐 사용 개수 :", str(counts))
print("총 지폐 사용 개수 :", str(total_bills))


end_time = datetime.now()
elapsed = elapsed_time(start_time)
print("걸린 시간:", elapsed)
