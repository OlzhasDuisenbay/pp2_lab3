"""Write a function that accepts string from user, return a sentence with the
words reversed. We are ready -> ready are We"""
def reverse_words(sentence):
    a = sentence.split()
    i = 1
    for i in range(len(a)):
        i += 1
        print(a[-i],end=" ")
s = input("Enter a sentence:")
reverse_words(s)
#we are ready >>>ready are we
