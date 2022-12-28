import re

def is_fully_contained(person1, person2):
    if(int(person1[0]) <= int(person2[0]) and int(person1[1]) >= int(person2[1])):
        return True
    elif(int(person1[0]) >= int(person2[0]) and int(person1[1]) <= int(person2[1])):
        return True
    else:
        return False
    

def is_overlap(person1, person2):
    if(int(person1[1]) < int(person2[0]) and int(person1[1]) < int(person2[0])) or (int(person2[0]) < int(person1[0]) and int(person2[1]) < int(person1[0])):
        return False
    else:
        return True
    


person1 = []
person2 = []
sum = 0
with open('text.txt') as f:
    lines = f.readlines()
    for i in lines:
        pair = re.split(r",|-|\n", i)
        person1.clear()
        person2.clear()
        
        person1.append(pair[0])
        person1.append(pair[1]) 
        person2.append(pair[2])
        person2.append(pair[3])
        # print(person1,person2)
        if(is_overlap(person1, person2) is True):
          sum += 1
    
print(sum)