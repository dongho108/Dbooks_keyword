#-*-coding:utf-8-*-
import io
ids = open("/Users/dongho/Documents/Auto_Excel/straw.txt", "r", encoding="UTF-8")
srw = open("/Users/dongho/Documents/Auto_Excel/Baesongmemo.txt", "r", encoding='UTF-8')

ids.readlines()
srw.readlines()
i = 0
for id in ids:
    print(id)
    if '딸기' in srw[i]:
        print(i)
        print(id+"@naver.com", end=", ")
    i = i+1
ids.close()
srw.close()


# ids = ["딸기", "포도", "raed","딸기(ㅁㄴㅇ)"]
# for id in ids:
#     if '딸기' in id:
#         print(id)
