# Exercise 1: Sets
data = [3, 5, 7, 5, 9, 3]
unique_values = list(set(data))
print("Unique Values:", unique_values)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference (A - B):", A - B)
print("Symmetric Difference:", A ^ B)

text = "apple banana apple cherry banana"
unique_words = set(text.split())
print("Unique Words:", unique_words)
print("Number of Unique Words:", len(unique_words))

# Exercise 2: Dictionaries
student = {"name": "John", "age": 21, "courses": ["Math", "CS"]}
print("Student Dictionary:", student)

sentence = "hello world hello"
word_freq = {}
for word in sentence.split():
    word_freq[word] = word_freq.get(word, 0) + 1
print("Word Frequency:", word_freq)

squares = {x: x**2 for x in range(1, 6)}
print("Squares Dictionary:", squares)

# Exercise 3: Walrus Operator
while (n := int(input("Enter a number greater than 10: "))) <= 10:
    pass
print("Accepted number:", n)

# Exercise 4: Merge Dictionaries with Conflict Resolution
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = {}
for k in dict1.keys() | dict2.keys():
    if k in dict1 and k in dict2:
        merged[f"{k}_resolved"] = dict1[k] + dict2[k]
    else:
        merged[k] = dict1.get(k, dict2.get(k))
print("Merged Dictionary:", merged)
