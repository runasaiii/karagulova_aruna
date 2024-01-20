def reversed_str(w_list):
    result = ''
    i = len(w_list) - 1
    while i >= 0:
        result += w_list[i]
        i -= 1
    return result

def palindrome(word):
    reversed_word = reversed_str(w_list)
    return word == reversed_word

word = input("Enter a word: ")
w_list = [char for char in word]
is_palindrome = palindrome(word)
print(f"{word} is a palindrome: {is_palindrome}")
