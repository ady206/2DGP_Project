world = [ [], [], [] ]
collision_group = dict()

def add_object(o, depth):
    world[depth].append(o)

def add_objects(ol, depth):
    world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o
            return
    raise ValueError('Trying destroy non existing object')

def all_objects():
    for layer in world:
        for o in layer:
            yield o

def clear():
    for o in all_objects():
        del o
    for layer in world:
        layer.clear()

def add_collision_group(a, b, group):
    if group not in collision_group:
        collision_group[group] = [[], []]

    if a: # a가 있으면
        if type(a) == list:
            collision_group[group][0] += a
        else:
            collision_group[group][0].append(a)

    if b: # b가 있으면
        if type(b) == list:
            collision_group[group][1] += b
        else:
            collision_group[group][1].append(b)

def all_collision_pairs():
    # collision_group 이라는 딕셔너리에서, 각 리스트로부터 페어를 만들어서 보내준다.
    for group, pairs in collision_group.items(): # items() : key, value 전달
        for a in pairs[0]:
            for b in pairs[1]:
                yield a, b, group

def remove_collision_object(o):
    for pairs in collision_group.values(): # key:value에서 value에 해당되는 것만 가져온다
        if o in pairs[0]: pairs[0].remove(o)
        elif o in pairs[1]: pairs[1].remove(o)