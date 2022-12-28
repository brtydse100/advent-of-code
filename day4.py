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
with open('day4_input.txt') as f:
    lines = f.readlines()
    for i in lines:
        pair = re.split(r",|-|\n", i)
        person1.clear()
        person2.clear()
        
        for j in range(2):  
            person1.append(pair[j])
            person2.append(pair[j+2])
        # print(person1,person2)
        if(is_overlap(person1, person2) is True):
          sum += 1
    
print(sum)