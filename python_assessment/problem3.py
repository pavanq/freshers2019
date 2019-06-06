lexicographic_order = ['r', 'c', 't', 'a']
input_list = ['car', 'rat', 'cat']
# Assuming all the words in the input list contains alphabets from the lexicographic_order list of characters
sorted_list = sorted(input_list, key=lambda word: [lexicographic_order.index(c) for c in word])
print("The sorted list is {}".format(sorted_list))
