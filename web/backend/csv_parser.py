def parser(path='web/backend/files/123.csv'):
    result = {}
    with open(path, 'r') as f:
        flag = False
        count = 0
        for line in f.readlines():
            f = False
            if flag:
                stack = []
                cnt = 0
                for i in line:
                    # print(i)
                    if i == "'":
                        if not f: f = True
                        elif f:
                            f = False
                            if cnt == 0: id = ''.join(stack)
                            if cnt == 1: text = ''.join(stack)
                            if cnt == 2: instruction = ''.join(stack)
                            stack = []
                            cnt += 1
                        continue
                    if f: stack.append(i)
                result[id]=[text,instruction]
            flag = True
    return result

if __name__ == '__main__': print(parser())
