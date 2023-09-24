class Table:
    def __init__(self, father, state):
        self.father = father
        self.state = state

    @staticmethod
    def findZero(pieces):
        for i in range(9):
            if pieces[i] == 0:
                return i

    @staticmethod
    def getChildren(pieces):
        position = Table.findZero(pieces)
        stepsArray = []
        if position == 0:
            stepsArray.append(Table.getPossibility(pieces, 0, 1))
            stepsArray.append(Table.getPossibility(pieces, 0, 3))
        elif position == 1:
            stepsArray.append(Table.getPossibility(pieces, 1, 0))
            stepsArray.append(Table.getPossibility(pieces, 1, 2))
            stepsArray.append(Table.getPossibility(pieces, 1, 4))
        elif position == 2:
            stepsArray.append(Table.getPossibility(pieces, 2, 1))
            stepsArray.append(Table.getPossibility(pieces, 2, 5))
        elif position == 3:
            stepsArray.append(Table.getPossibility(pieces, 3, 0))
            stepsArray.append(Table.getPossibility(pieces, 3, 4))
            stepsArray.append(Table.getPossibility(pieces, 3, 6))
        elif position == 4:
            stepsArray.append(Table.getPossibility(pieces, 4, 1))
            stepsArray.append(Table.getPossibility(pieces, 4, 3))
            stepsArray.append(Table.getPossibility(pieces, 4, 5))
            stepsArray.append(Table.getPossibility(pieces, 4, 7))
        elif position == 5:
            stepsArray.append(Table.getPossibility(pieces, 5, 2))
            stepsArray.append(Table.getPossibility(pieces, 5, 4))
            stepsArray.append(Table.getPossibility(pieces, 5, 8))
        elif position == 6:
            stepsArray.append(Table.getPossibility(pieces, 6, 3))
            stepsArray.append(Table.getPossibility(pieces, 6, 7))
        elif position == 7:
            stepsArray.append(Table.getPossibility(pieces, 7, 4))
            stepsArray.append(Table.getPossibility(pieces, 7, 6))
            stepsArray.append(Table.getPossibility(pieces, 7, 8))
        elif position == 8:
            stepsArray.append(Table.getPossibility(pieces, 8, 5))
            stepsArray.append(Table.getPossibility(pieces, 8, 7))

        return stepsArray

    @staticmethod
    def getPossibility(pieces, position1, position2):
        change = pieces.copy()
        change[position1] = pieces[position2]
        change[position2] = pieces[position1]
        return change

initialState = [0, 1, 3, 4, 2, 6, 7, 5, 8]
objective = [1, 2, 3, 4, 5, 6, 7, 8, 0]
actualState = initialState
flag = 1
resolution = []

newFathers = []
children = []
fathers = []
fathers.append(Table([], initialState))

while flag:
    for father in fathers:
        aux = father.state
        children = father.getChildren(father.state)
        for child in children:
            newFathers.append(Table(father, child))
            if child == objective:
                flag = 0
                break
        if flag == 0:
            break
    fathers = newFathers
    newFathers = []

father = fathers[-1]


while father.father != []:
    resolution.append(father.state)
    father = father.father
resolution.append(father.state)

for array in resolution:
    print(array)