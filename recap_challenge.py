# """
# Exercise 1:
# Write a program that takes a list of numbers and prints the sum of all the numbers in the list.
# """
list_of_numbers = [2, 3, 5, 7, 11, 13, 17]
print(sum(list_of_numbers))

# alternate

sum_of_numbers = 0
for number in list_of_numbers:
    sum_of_numbers += number
print(sum_of_numbers)

# """
# Exercise 2:
# Write a program that takes a list of strings and prints the length of each string in the list.
# """

list_of_strings = ["the", "quick", "brown", "fox", "jumped"]
for string in list_of_strings:
    print("The length of", string, "is", len(string))

# """
# Exercise 3:
# Write a program that prompts the user to enter 5 names and stores them in a list. Then, print the list in alphabetical order.
# HINT: Use a range(5) with a for loop to loop 5 times
# HINT: To get user input and store it in a variable: name = input("Enter a name: ") 
# """

list_of_names = []
for name in range(5):
    name = input("Enter a name: ") 
    list_of_names.append(name)
list_of_names_sorted = sorted(list_of_names)
print("The list of names sorted alphabetically is:", list_of_names_sorted)

# # """
# Exercise 4:
# Write a program that takes a list of numbers and prints the largest and smallest numbers in the list.
# HINT: min and max are built-in Python functions
# """
list_of_numbers = [2, 3, 5, 7, 11, 13, 17]

min_number = min(list_of_numbers)
max_number = max(list_of_numbers)
print("The smallest number is ", min_number)
print("The largest number is ", max_number)

# """
# Exercise 5:
# Write a program that takes a list of integers and prints the average of the numbers in the list.
# """
average_number = sum(list_of_numbers) / len(list_of_numbers)
print("The average of the listed numbers is:", average_number)

# Alternative below

sum = 0
for n in list_of_numbers:
    sum += n
average_sum = sum / len(list_of_numbers)
print("The average of the listed numbers is:", average_sum)

# """
# Exercise 6:
# Write a program that takes a list of integers and removes all the duplicates, printing the updated list.
# HINT: Python's in-built set function will remove duplicates from a list
# """

list_of_number_dupes = [2, 2, 3, 3, 5, 5, 7, 7, 11, 17, 13, 17]
no_duplicates = set(list_of_number_dupes)

print(no_duplicates)

# """
# Exercise 7:
# Write a program that prompts the user to enter a sentence and prints the sentence in reverse order.
# """

sentence_input = input("Please enter a sentence:")

word_list = sentence_input.split()
reversed_list = reversed(word_list)
reversed_sentence = " ".join(reversed_list)
print(reversed_sentence)

# """
# BONUS CHALLENGE!
# Write a program that prompts the user to enter a sentence and counts the frequency of each word in the sentence using a dictionary.
# HINT: Python's split() method will turn a set into a List
# """
