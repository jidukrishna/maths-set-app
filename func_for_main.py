# set string to dict convertor
def ld(d):
    a = d.lstrip('{').rstrip('}').split(',')
    op = []
    for i in a:
        try:
            if float(i) % 1 == 0:
                op.append(int(i))
            else:
                op.append(float(i))
        except:
            pass
    return op


# duplicate remover

def delete(list):
    try:
        return str([*set(list)]).replace('[', '{').replace(']', '}')
    except:
        return 'not valid'


# union func

def union(list1, list2):
    return [*set(list1 + list2)]


# intersection func
def inter(list1, list2):
    return str([*set([i for i in list1 if i in list2] + [i for i in list2 if i in list1])]).replace('[', '{').replace(
        ']', '}')


# subset checker
def ch(list, elem):
    c = 1
    for i in elem:
        if i in list:
            pass
        else:
            c = 0
    if c == 0:
        return False
    else:
        return True


# set diff

def setd(list1, list2):
    return str([i for i in list1 if i not in list2]).replace('[', '{').replace(']', '}')


