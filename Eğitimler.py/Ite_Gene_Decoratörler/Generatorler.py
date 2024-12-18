
def Numbers(Number):
    Liste = []
    for i in range(1,Number + 1):
        if i%2 == 0:
            Liste.append(i)
    return Liste

def Generator(Number):
    for i in range(1,Number + 1):
        if i%2 == 0:
            yield i

for i in Generator(100):
    print(i)