def check_palindrome(word_string):
    new_word = word_string.lower()

    l = 0
    r = len(new_word) - 1

    while l < r:
        if new_word[l] != new_word[r]:
            return False
        else:
            l += 1
            r -= 1
    return True















































    # #Solution 1
    # word_string = word_string.lower()
    # i = 0
    # j = len(word_string) - 1

    # while j != 0:
    #     if word_string[i] == word_string[j]:
    #         i += 1
    #         j -= 1
    #         continue
    #     return False
    # return True



    # #Solution 2
    # # word_string = word_string.lower()
    # # return word_string == word_string[::-1]


    # #Solution 3
    # # word_string = word_string.replace(" ", "")
    # # word_list = [word for word in word_string.lower()]
    # # reverse_string = []
    # # r_index = -1

    # # for word in word_list:
    # #     reverse_string.append(word_list[r_index])
    # #     r_index -= 1

    # # if word_list == reverse_string:
    # #     return True
    # # return False

            


