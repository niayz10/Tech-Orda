n = int(input())
all_minutes = n * 45 + (((n - 1) // 2) * 15) + ((n - 1) // 2 + (n - 1) % 2) * 5
hours = all_minutes // 60 + 9
minutes = all_minutes % 60

print(hours, minutes)
