import MBranch

MBranch.init_stores()
print("\r\nStore A")
for day in MBranch.list_store_a:
    print(day.day)
    print(day.revenue)

print("\r\nStore B")
for day in MBranch.list_store_b:
    print(day.day)
    print(day.revenue)

print("\r\nStore C")
for day in MBranch.list_store_c:
    print(day.day)
    print(day.revenue)



