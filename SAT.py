import random
import time


class SAT:

    def __init__(self, filename):
        self.filename = filename
        self.assignment = None
        self.clauses = list()
        reader = open(filename)
        for line in reader:
            self.clauses.append(line.split())
        reader.close()


    # Checks a specific clause and returns whether or not it is satisfied
    def isSatisfied(self, clause, assignment):
        for value in clause:
            if value[0] == "-":
                if not assignment[int(value[1:])]:
                    return True
            else:
                if assignment[int(value)]:
                    return True
        return False

    # Checks if the current assignment satisfies all clauses
    def isComplete(self, assignment):
        for clause in self.clauses:
            if not self.isSatisfied(clause, assignment):
                return False
        return True

    # Returns a list of the variables, which, if they have their value switched in the assignment,
    # Will satisfy the most clauses in the Knowledge Base
    def topscores(self, assignment):
        scorekeeper = {}

        for x in range(1000):
            scorekeeper[x] = 0
            if x > 100:
                if int(str(x)[0]) > 0 and int(str(x)[1]) > 0 and int(str(x)[2]) > 0:
                    assignment[x] = not assignment[x]
                    for clause in self.clauses:
                        if self.isSatisfied(clause, assignment):
                            scorekeeper[x] = scorekeeper[x] + 1
                    assignment[x] = not assignment[x]

        returner = list()
        maxscore = -1
        for x in range(1000):
            if scorekeeper[x] == maxscore:
                returner.append(x)
            elif scorekeeper[x] > maxscore:
                maxscore = scorekeeper[x]
                returner.clear()
                returner.append(x)

        return returner


    # From the variables present in one of the unsatisfied clauses, selects the one that, if changed, will
    # Cause the most clauses to be correct
    def WalkSATScores(self, assignment):

        # All unsatisfied clauses
        unsatisfied = list()
        for clause in self.clauses:
            if not self.isSatisfied(clause, assignment):
                unsatisfied.append(clause)

        selected = random.choice(unsatisfied)
        selected = self.formatVariables(selected)

        rand = random.random()
        if rand < .3:
            returner = list()
            for x in selected:
                returner.append(int(x))
            return returner

        # Keeps scores for all of the variables used in scorekeeper, and scores each based on satisfied clauses
        scorekeeper = {}
        for x in selected:
            scorekeeper[x] = 0
            assignment[int(x)] = not assignment[int(x)]
            for clause in self.clauses:
                if self.isSatisfied(clause, assignment):
                    scorekeeper[x] = scorekeeper[x] + 1
            assignment[int(x)] = not assignment[int(x)]

        # Creates a list of the highest scoring variables to return.
        returner = list()
        maxscore = -1
        for x in selected:
            if scorekeeper[x] == maxscore:
                returner.append(int(x))
            elif scorekeeper[x] > maxscore:
                maxscore = scorekeeper[x]
                returner.clear()
                returner.append(int(x))

        return returner

    # Removes the "-" from the front of any of the variables in the list. Used to switch
    # formatting for the clauses to a list of variables used in the clause
    def formatVariables(self, selected):
        returner = list()
        for x in selected:
            if x[0] == "-":
                returner.append(x[1:])
            else:
                returner.append(x)
        return returner



    # Randomly generates a starting assignment, then will randomly change variable's values,
    # Sometimes completely randomly and sometimes based on the variable changes that result
    # in the most clauses that are True
    def GSAT(self):
        starttime = time.time()
        assignment = list()
        for x in range(1000):
            rand = random.random()
            if rand < .5:
                assignment.append(True)
            else:
                assignment.append(False)

        threshold = .7
        for switches in range(500000):
            if self.isComplete(assignment):
                self.assignment = assignment
                print("total switches: " + str(switches))
                print("total time: " + str(time.time() - starttime))
                return True
            rand = random.random()
            if rand > threshold:
                row = random.randint(1, 9)
                col = random.randint(1, 9)
                val = random.randint(1, 9)
                switcher = int(str(row) + str(col) + str(val))
                assignment[switcher] = not assignment[switcher]
            else:
                candidates = self.topscores(assignment)
                switcher = random.choice(candidates)
                assignment[switcher] = not assignment[switcher]
        print("failed to solve in 500,000 moves")
        return False

    # Randomly generates a starting assignment, then randomly changes variable's values,
    # sometimes completely randomly, and sometimes intelligently, based off the WalkSATScores method.
    # Exactly the same at the GSAT method, except for line 169
    def WalkSAT(self):
        starttime = time.time()
        assignment = list()
        for x in range(1000):
            rand = random.random()
            if rand < .5:
                assignment.append(True)
            else:
                assignment.append(False)

        for switches in range(500000):
            if self.isComplete(assignment):
                self.assignment = assignment
                print("total switches: " + str(switches))
                print("total time: " + str(time.time() - starttime))
                return True
            candidates = self.WalkSATScores(assignment)
            switcher = random.choice(candidates)
            assignment[switcher] = not assignment[switcher]
        print("failed to solve in 500,000 moves")
        return False


    # Writes the solution into a file by writing the variables that are True
    def write_solution(self, filename):
        file = open(filename, "w")

        for x in range(1000):
            if x > 100:
                if int(str(x)[0]) > 0 and int(str(x)[1]) > 0 and int(str(x)[2]) > 0:
                    if self.assignment[x]:
                        file.write(str(x) + '\n')
