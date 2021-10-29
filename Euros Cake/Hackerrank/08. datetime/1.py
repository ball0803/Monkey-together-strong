from calendar import weekday
m, d, y = map(int, input().split())
day = weekday(y, m, d)
n = ('MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY')
print(n[day])
