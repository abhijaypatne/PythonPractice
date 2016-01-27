
classes = {}


def printClasses(id):
    for key in classes.keys():
        if(key.find(id) >= 0):
            print(key, classes.get(key))
        else:
            print("No Course %s classes taken" % (id) )
            break

def addClass(id, name):
    classes[id] = name

def main():
    classes['CS412'] = "Machine Learning"
    classes['CS587'] = "Computer Security"
    classes['CS474'] = "Object-Oriented Languages"
    addClass('IDS561', "Analytics for Big Data")
    addClass('CS553', "Distributed Systems")
    printClasses('9')

if __name__=="__main__":
    main()