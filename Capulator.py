
class Capculator:
    print('Welcome to the CAPulator!')
    print('')
    
    print('To use: type calc.(command)')
    print('')
    
    print('Commands:')
    print('')
    
    print('1) calc.add(grades) and calc.remove(grades) to add/subtract respectively [FOR 4 MC MODULES]')
    print('2) calc.addspec((grade,MC),(grade,MC)...) or calc.removespec(<same format>) to remove Non- 4 MC Modules')
    print('3) calc.CAP() to calculate your CAP.')
    print('4) calc.grades() to display a list of your attained grades.')
    print("5) calc.target(<key target here>) to find out how many A's you need for your target grade")
    print('6) calc.reset() to reset the CAPculator')
    print('')
    print('')
          
    def __init__(self):
        self.cap=0
        self.num=0
        self.denom=0
        self.summary=[]
        self.SUsummary=[]
        self.lastCommand=[]

    def undo(self):
        for i in self.lastCommand:
            self.removeUndo(i)
        self.lastCommand =[]
        print('Your new CAP is '+str(self.cap))
        

    def add(self,*grades):      ## Made for speed - Assumes all modules 4 MC
        """Example: calc.add('B'), calc.add('A','B','C+')"""
        if grades == ():
            return 'Please enter at least one grade that you wish to add.'
        for entry in grades:
            if self.checker(entry):
                    self.num += self.checker(entry)*4
                    self.denom += 4
                    self.summary += [entry]
        if self.denom !=0:
            self.cap = (self.num/self.denom)
            print('Your new CAP is '+str(self.cap))
            self.lastCommand=list(grades)
        else:
            print('Your new CAP is 0')

    def remove(self,*grades):     ## Made for speed - Assumes modules are 4 MC
        """Example: calc.remove('B'), calc.remove('A','B','C+')"""
        if self.cap == 0:
            return 'CAP = 0, Nothing left to remove!'
        for grade in grades:
            if grade not in self.summary:
                return 'Incorrect entry: You do not have one or more of the grades that you have entered'
        for grade in grades:
            self.num -= self.checker(grade)*4
            self.denom-=4
            self.summary.remove(grade)
        if self.denom !=0:
            self.cap = (self.num/self.denom)
            print('Your new CAP is '+str(self.cap))
        else:
            print('Your new CAP is 0')
            
    ##AUXILARY FUNCTION - USED BY UNDO
    def removeUndo(self,*grades):     ## Made for speed - Assumes modules are 4 MC
        """Example: calc.remove('B'), calc.remove('A','B','C+')"""
        if self.cap == 0:
            return 'CAP = 0, Nothing left to remove!'
        for grade in grades:
            if grade not in self.summary:
                return 'Incorrect entry: You do not have one or more of the grades that you have entered'
        for grade in grades:
            self.num -= self.checker(grade)*4
            self.denom-=4
            self.summary.remove(grade)
        if self.denom !=0:
            self.cap = (self.num/self.denom)
        
    ##AUXILARY FUNCTION. USED BY STRESSTEST
    def removeStressTest(self,*grades):     ## Made for speed - Assumes modules are 4 MC
        """Example: calc.remove('B'), calc.remove('A','B','C+')"""
        if self.cap == 0:
            return 'CAP = 0, Nothing left to remove!'
        for grade in grades:
            if grade not in self.summary:
                return 'Incorrect entry: You do not have one or more of the grades that you have entered'
        for grade in grades:
            self.num -= self.checker(grade)*4
            self.denom-=4
            self.summary.remove(grade)
        if self.denom !=0:
            self.cap = (self.num/self.denom)
            

    def addspec(self,grades):           ##For non 4 MC modules
        """For modules that are not 4 MC's each. One argument in the
        format of (Grade,MC). Eg, ((A+,6),(B,5))"""
        one = True
        for i in grades:
            if type(i) == tuple:
                one=False
                break
                
        if one == True:
            self.num+=(self.checker(grades[0])*grades[1])
            self.denom+= grades[1]
            self.summary+= [grades[0]]
            self.cap = self.num/self.denom
        else:
            for entry in grades:
                self.num+=(self.checker(entry[0])*entry[1])     
                self.denom+= entry[1]                           
                self.summary+= [entry[0]]
            self.cap = self.num/self.denom
        print('Your new CAP is '+str(self.cap))

    def removespec(self,grades):        ##For non 4 MC modules
        one = True
        for i in grades:
            if type(i) == tuple:
                one=False
                break
                
        if one == True:
            self.num-=(self.checker(grades[0])*egrades[1])
            self.denom-= grades[1]
            self.summary.remove(grades[0])
        else:
            for grade in grades:
                if grade[0] not in self.summary:
                    return 'Incorrect entry, You do not have one or more of the grades that you have entered'
            for entry in grades:
                    self.num-=(self.checker(entry[0])*entry[1])
                    self.denom-= entry[1]
                    self.summary.remove(entry[0])
        self.cap = self.num/self.denom
        print('Your new CAP is '+str(self.cap))

    def SU(self,name,oldgrade):
        self.SUsummary+=[[name,oldgrade]]
        self.summary+=['S']
            
    def CAP(self):
        return self.cap

    def stats(self):
        print('Your CAP is '+str(self.cap))
        print(self.grades())
        print(self.SUgrades())
        
    def grades(self):
        print( 'Summary of your grades: ')
        return self.summary
    
    def SUgrades(self):
        print('Summary of your SU mods:')
        return self.SUsummary
    
    def stressTest(self):
        print('Adding 5 A-:')
        calc.add('A-','A-','A-','A-','A-')
        calc.removeStressTest('A-','A-','A-','A-','A-')
        print("Adding 5 B+:")
        calc.add('B+','B+','B+','B+','B+')
        calc.removeStressTest('B+','B+','B+','B+','B+')
        print("Adding 3 B+ and 2 C+:")
        calc.add('B+','B+','B+','C+','C+')
        calc.removeStressTest('B+','B+','B+','C+','C+')
        print("Adding 2 B+,1 B, and 2 C+:")
        calc.add('B+','B+','B','C+','C+')
        calc.removeStressTest('B+','B+','B','C+','C+')

    def reset(self):
        self.num=0
        self.denom=0
        self.summary = []
        self.SUsummary=[]
        return 'All stored information reset!'

    def target(self,targetcap):
        if self.cap >= targetcap:
            return 'You already have that CAP! Congratulations!'
        else:
            cap=self.cap
            num1=self.num
            denom1=self.denom
            A=0
            while cap < targetcap:
                num1 += 5*4
                
                denom1 += 4
                A+=1
                cap = num1/denom1
                if A > 20:
                    break
            if A > 20:
                return "More than 20 A's required! Would you like to pick a lower target?"
            if A == 1:
                return "You need approximately 1 A to achieve your target CAP!"
            else:
                return "You need approximately " + str(A) + " A's to achieve your target CAP!"

    def targetCUSTOM(self,targetcap,grade):
        if self.cap >= targetcap:
            return 'You already have that CAP! Congratulations!'
        else:
            cap=self.cap
            num1=self.num
            denom1=self.denom
            value=self.checker(grade)
            selectedgrade=0
            if targetcap > self.checker(grade):
                return 'Not possible, The grade you have selected has a CAP value lower than your target. Please choose a higher grade'
            while cap < targetcap:
                num1 += value*4
                
                denom1 += 4
                selectedgrade+=1
                cap = num1/denom1
                if selectedgrade > 25:
                    break
            if selectedgrade > 25:
                return "More than 25 " + grade + "'s required! Would you like to pick a lower target?"
            if selectedgrade == 1:
                return "You need approximately 1 " + grade + " to achieve your target CAP!"
            else:
                return "You need approximately " + str(selectedgrade) + " " + grade + "s to achieve your target CAP!"

    def checker(self,grade):
        if grade == 'A+' or grade == 'A':
            return 5
        elif grade == 'A-':
            return 4.5
        elif grade == 'B+':
            return 4.0
        elif grade == 'B':
            return 3.5
        elif grade == 'B-':
            return 3.0
        elif grade == 'C+':
            return 2.5
        elif grade == 'C':
            return 2.0
        elif grade == 'D+':
            return 1.5
        elif grade == 'D':
            return 1.0
        elif grade == 'F':
            return 0
        else:
            return False
        
calc= Capculator()
calc.add('A','A','A-','A-','A-','B+','A','A+','A','B+','B-')
calc.SU('Matrix Algebra','B+')
calc.SU('Calculus For Computing','B')
calc.SU('CS1020','B')
print(calc.grades())
print(calc.SUgrades())
