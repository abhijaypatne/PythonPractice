NAMES = ['Alice', 'Bob', 'Cathy', 'Dan', 'Ed', 'Frank', 'Gary', 'Helen', 'Irene', 'Jack', 'Kelly', 'Larry']
AGES = [20, 21, 18, 18, 19, 20, 20, 19, 19, 19, 22, 19]
peopleDictionary = {}

## Create a dictionary with NAMES and AGES mapping
def combineLists():
    for (key, value) in zip(NAMES, AGES):
        peopleDictionary[key] = value

## Return list of people with specified age
def people(age):
    result = []
    for name in peopleDictionary.keys():
        if (peopleDictionary.get(name) == age):
            result.append(name)
    return result

def runTestCases():
    print ('Dan' in people(18) and 'Cathy' in people(18))
    print ('Ed' in people(19) and 'Helen' in people(19) and\
           'Irene' in people(19) and 'Jack' in people(19) and 'Larry'in people(19))
    print ('Alice' in people(20) and 'Frank' in people(20) and 'Gary' in people(20))
    print (people(21) == ['Bob'])
    print (people(22) == ['Kelly'])
    print (people(23) == [])

def main():
    print("Creating dictionary")
    combineLists()
    print("Dictionary: ", peopleDictionary)
    print("Running Testcases")
    runTestCases()

if __name__=="__main__":
    main()

