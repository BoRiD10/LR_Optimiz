import random
import time


def identification():
    key = list(Start_Key.replace(" ", ""))
    length_key = len(key)
    return key, length_key


def formData():
    Symbol = []
    for i in range(1040, 1103):
        Symbol.append(chr(i))
    Symbol.append('ё')
    Symbol.append('Ё')
    Symbol.append(' ')
    if Part == 1:
        return Symbol
    if Part == 2:
        for i in range(44, 47):
            Symbol.append(chr(i))
        Symbol.append('!')
        Symbol.append(chr(171))
        Symbol.append(chr(187))
        Symbol.append(':')
        Symbol.append(';')
        Symbol.append('?')
        return Symbol
    if Part == 3:
        for i in range(65, 91):
            Symbol.append(chr(i))
        for i in range(97, 123):
            Symbol.append(chr(i))
        return Symbol


def population():
    AllWord = []
    Interval = len(Symbol)
    for i in range(0, 500):
        Word = ""
        for j in range(0, Lenght_Key):
            Word = Word + str(Symbol[random.randint(0, Interval - 1)])
        AllWord.append(Word)
    return AllWord


def Selection(AllWord):
    Diction = {}
    for j in AllWord:
        Value = 0
        Word = list(j)
        for i in range(0, Lenght_Key):
            if Word[i] == Key[i]:
                Value += 1
        Diction[j] = Value
    list_keys = sorted(Diction.items(), key=lambda kv: kv[1], reverse=True)
    Diction = dict(list_keys)
    C = list_keys[0]
    if C[1] == Lenght_Key:
        print("You are Win!!\n" + "You have: " + str(C[0]))
        return True, C[0]
    else:
        return False, Diction


def generate_new_population(Diction):
    D = []
    parents = []
    Mutant = []
    Alliens = []
    len_parents = int(0.4 * len(Diction))
    len_mutants = int(0.9 * len(Diction))
    for key in Diction.keys():
        D.append(key)
    for i in range(0, len_parents):
        parents.append(D[i])
    for j in range(len_parents, len_mutants):
        Mutant.append(D[j])
    for k in range(len_mutants, len(D)):
        Alliens.append(D[k])
    New_ind = reproduction(parents)
    Mut_ind = mutation(Mutant)
    All_ind = allien(Alliens)
    New_population = []
    for i in range(0, len(New_ind)):
        New_population.append(New_ind[i])
    for j in range(0, len(Mut_ind)):
        New_population.append(Mut_ind[j])
    for k in  range(0, len(All_ind)):
        New_population.append(All_ind[k])
    return New_population


def reproduction(Parents):
    P = 0.7
    for k in range(0, len(Parents)):
        rand = random.random()
        i = random.randint(0, len(Parents) - 1)
        j = random.randint(0, len(Parents) - 1)
        if rand < P:
            ind1 = Parents[i]
            ind2 = Parents[j]
            ind1 = list(ind1)
            ind2 = list(ind2)
            ind3 = []
            for h in ind1:
                ind3.append(h)
            r = random.randint(1, len(ind1))
            for n in range(0, r):
                ind1[n] = ind2[n]
                ind2[n] = ind3[n]
            Parents[i] = ''.join(ind1)
            Parents[j] = ''.join(ind2)
    return Parents


def mutation(Mutant):
    P = 0.4
    Interval = len(Symbol)
    for i in range(0, len(Mutant)):
        m = list(Mutant[i])
        for j in range(0, len(m)):
            if P > random.random():
                m[j] = Symbol[random.randint(0, Interval - 1)]
        Mutant[i] = ''.join(m)
    return Mutant

def allien(Alliens):
    P = 0.5
    Interval = len(Symbol)
    for i in range(0, len(Alliens)):
        a = list(Alliens[i])
        if P > random.random():
            for j in range(0, len(a)):
                a[j] = Symbol[random.randint(0, Interval - 1)]
        Alliens[i] = ''.join(a)
    return Alliens

StartTime = time.process_time()
# Start_Key = 'нога'
# Start_Key = 'БЛоК'
Start_Key = 'В бреду, дескать!.. Ха-ха-ха! Он про весь вечер вчерашний знает! Про приезд матери не знал!.. А ведьма и число прописала карандашом!..'
# Start_Key = 'Встретились в Crocus City холле'
Part = 2
k = Start_Key.split(" ")
if len(k) > 1:
    mass = ""
    for i in range(0, len(k)):
        Start_Key = k[i]
        Key, Lenght_Key = identification()
        Symbol = formData()
        count = 1
        first_population = population()
        Win, Dict = Selection(first_population)
        while not Win:
            Win, Dict = Selection(generate_new_population(Dict))
            count += 1
        mass += Dict + " "
    print(mass)
    EndTime = time.process_time()
    Time = EndTime - StartTime
    print("Time: " + str(Time))
else:
    Key, Lenght_Key = identification()
    Symbol = formData()
    count = 1
    first_population = population()
    Win, Dict = Selection(first_population)
    while not Win:
        Win, Dict = Selection(generate_new_population(Dict))
        count += 1
    print(count)
    EndTime = time.process_time()
    Time = EndTime - StartTime
    print("Time: " + str(Time))
