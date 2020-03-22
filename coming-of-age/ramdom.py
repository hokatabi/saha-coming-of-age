import random
import sentence

def ran_sentence(listname, num=None):
    
    if num is None:
        num = len(listname)

    print(num)
    print (random.randint(0, num))
    return str(listname[random.randint(0, num-1)])

content = ran_sentence(sentence.寝る5分前)
print(content)
