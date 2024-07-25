""""
for i in readlines():
    a[] = i
for i in range(500000001):
    if a[i] == "2":
        if a[i+1] == "0":
            if a[i+2] == "2":
                if a[i+3] == "2":
                    if (int(a[i+4]) *10 + int(a[i+5])) <= 12:
                        if(int(a[i+6] * 10)+ int(a[i+7]))) <= 31:
"""


#在pai中寻找日期
f = open("pi50.4.bin", "rb")
dbuff = f.read()
s=("".join((f"{d:02x}" for d in dbuff))).encode()#将读进来数据变成字节串
d1 = datetime.date(2022, 1, 1)
found = 0
for n in range(365):
    day = ((d1 + datetime.timedelta(days=n)).strftime("%Y%m%d")).encode()
    if day in s:
        found += 1
                                