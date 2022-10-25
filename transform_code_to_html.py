s = "f=f.reset_index(drop=True)"
# s = "a=1"

key_word_list = ["if", "for", "in", "def", "class", 
                "return", "print", "else", "try", "except", 
                "yield", "continue", "break", "while", "and", 
                "not", "or"]

operator_list = ['+', '-', '*', '/', '=', 
                '<', '>', '%', '&', '|']

value_list = ['0', '1', '2', '-1', 'None', 'True', 'Flase']

# for i in key_word_list:
#     s = s.replace(i, "<code class=\"key_word\">{}</code>".format(i))

# for i in operator_list:
#     s = s.replace(i, "<code class=\"operator\">{}</code>".format(i))

# for i in value_list:
#     s = s.replace(i, "<code class=\"value\">{}</code>".format(i))

left, right = 0, 1
i, j = 0, 1
adds = 1
while left<len(s)-1:
    while right<=len(s):
        if s[left:right] in operator_list:
            s = s[:left] + "<code class=\"operator\">" + s[left:right] + "</code>" + s[right:]
            adds += 31
            right += 30
            left = right
            right += 1
        elif s[left:right] in key_word_list and not ord(s[right])>=65 and not ord(s[right])<=122:
            s = s[:left] + "<code class=\"key_word\">" + s[left:right] + "</code>" + s[right:]
            adds += 31
            right += 30
            left = right
            right += 1
        elif s[left:right] in value_list:
            s = s[:left] + "<code class=\"value\">" + s[left:right] + "</code>" + s[right:]
            adds += 30
            right += 29
            left = right
            right += 1
        else:
            right += 1
    i += adds
    j = i + 1
    left = i
    right = j
    adds = 1
    


print(s)
