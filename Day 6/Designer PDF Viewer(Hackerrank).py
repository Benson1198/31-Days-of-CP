h_line = input()
h_arr = [int(y) for y in h_line.split()]
word = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

width = len(word)

max_height = 0

for i in range(width):
    ind = alphabet.find(word[i])
    temp_height = h_arr[ind]
    if temp_height > max_height:
        max_height = temp_height

length = max_height

area = int(max_height*width)
print(area)