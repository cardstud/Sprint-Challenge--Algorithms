'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    th = 0

    # since th is 2 letters, any word less than 2 letters means there are none
    if len(word) < 2:
        return 0

    # search for 'th' in the string
    if word[:2] == 'th':
        th = th + 1

    # the recursive portion to continue through the string
    th = th + count_th(word[1:])
    return th

# test it
print("The number of times 'th' occurs in your string is: ", count_th("welcomethtomythhousethopethnupthechampagne,popthIt'smyhouse,comeon,turnitupth"))