i = 1
while i <= 5:
    n = int(input("ป้อนตัวเลขนะหว่าง 1-10 "))
    if n > 10:
        print("ป้อนให้มันถูกๆดิ 1-10 อ่ะ")
        continue
    if n <= 10:
        j = n * i
        print("ผลคูณระหว่าง %d x %d = "%(i,n),j)
    i += 1
