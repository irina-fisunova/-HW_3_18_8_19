tiket = int(input("Введите количество билетов:   "))
P = []
count = 0

while count < tiket:
    try:
        age = int(input())

        if age <= 0 or age > 100:
            raise ValueError("Тебе не может быть столько лет. Введите корректный возраст:   ")

    except ValueError as error:
        print(error)

    else:
        count = count + 1
        P.append(age)

tiket_18 = 0
tiket_18_25 = 990
tiket_25 = 1390
sum = 0

for i in range(tiket):
    if P[i] < 18:
        sum = sum + tiket_18
    elif P[i] >= 18 and P[i] < 25:
        sum = sum + tiket_18_25
    elif  P[i] >= 25:
        sum = sum + tiket_25

discount = 0

if tiket > 3:
    discount = sum * 0.1
    sum = sum - discount

print("Сумма к оплате:   ", sum)

if discount != 0:
    print("Скидка составила:   ", discount)