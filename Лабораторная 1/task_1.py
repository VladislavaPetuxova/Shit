numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

for i in range(len(numbers)):
    if numbers[i]==None:
        number_dr=numbers[:i]+numbers[(i+1):]
        numbers[i] = sum(number_dr)/len(numbers)

print("Измененный список:", numbers)
