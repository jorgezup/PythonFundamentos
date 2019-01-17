def askNum():
    while True:
        try:
            num = int(input())
        except:
            break
        return num

num = askNum()
i = 1
lista=[]
tot=0
while i< num+1:
    lista.append(i)
    i +=1

for num in lista:
   for cont in range(1, num+1):
       print("num {}".format(num))
       if num%cont == 0:
        tot+=1
