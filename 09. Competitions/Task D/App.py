# TIME LIMIT

def is_opening(tag):
    return tag[:2] != '</' and tag[0] == '<' and tag[-1] == '>'


def is_closing(tag):
    return tag[:2] == '</' and tag[-1] == '>'


def get_closing(tag):
    return tag[0] + '/' + tag[1:]


def is_matched(expression):
    queue = []

    for letter in expression:
        if is_opening(letter):
            queue.append(get_closing(letter))
        elif is_closing(letter):
            if not queue or letter != queue.pop():
                # print(letter)
                return False
    # print(queue)
    return not queue


x = int(input())
result = []

for test in range(x):
    s = int(input())
    tags = []
    for i in range(s):
        tag = input()
        tags.append(tag.upper())

    try:
        if is_matched(tags):
            flag = True
            result.append('CORRECT')
            continue
        else:
            flag = False
            for i in range(s):
                tmp = tags[:i] + tags[i+1:]
                if is_matched(tmp) and not flag:
                    flag = True
                    result.append('ALMOST ' + tags[i])
                    break

        if not flag:
            result.append('INCORRECT')
    except:
        result.append('INCORRECT')

print(*result, sep='\n')

# 3
# 4
# <X >
# <Y >
# </Y >
# </X >
# 5
# <HTML >
# <biba >
# </BIBA >
# </KUKA >
# </HTML >
# 6
# <HTML >
# <TAG >
# <button >
# </BUTTON >
# <TAG >
# </html >
