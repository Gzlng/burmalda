import random
import time

symbols = ["🍒", "🍋", "🔔", "💎", "7️⃣"]

def burmal():
    ransymb1 = random.choice(symbols)
    ransymb2 = random.choice(symbols)
    ransymb3 = random.choice(symbols)
    burmalda_list = [ransymb1, ransymb2, ransymb3]
    return burmalda_list

while True:
    burmalda = burmal()
    print(burmalda)
    time.sleep(0.4)
    if burmalda[0] == burmalda[1] == burmalda[2]:
        break

print('Ты просто босс!')