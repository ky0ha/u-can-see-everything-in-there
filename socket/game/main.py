from random import sample

class NumGroup(object):
    def __new__(cls, *args):
        for i in args:
            if not isinstance(i, str):
                raise TypeError(f"argments must be 'str' not '{i.__class__.__name__}'")
        return object.__new__(cls)
    
    def __init__(self, question):
        self.result = question
    
    def __str__(self):
        return self.result
    
    def guess(self, answer:str):
        hit, blew = 0, 0
        for i in range(3):
            if answer[i]==self.result[i]:
                hit+=1
            elif answer[i] in self.result:
                blew+=1
        return (hit, blew)

class Game(object):
    def __init__(self):
        self.question = NumGroup(''.join(str(i) for i in sample(range(10), 3)))
        self.history = []
    
    def submit(self, answer):
        if len(answer)==3:
            return self.question.guess(answer)
        else:
            print("need 3 numbers in answer")
            return (-1, -1)
    
    def show(self):
        result = f"{self.question}"
        print(result)
        return result

    def restart(self):
        self.__init__()
    
    def exit(self):
        exit()
        
# class SoloGame(Game):
#     __instance = None
    
#     def __init__(self):
#         if self.__instance==None:
#             self.question = NumGroup(''.join(str(i) for i in sample(range(10), 3)))
#             SoloGame.__instance=self
#         else:
#             raise Exception("SoloGame in running!")
    
#     def submit(self, answer):
#         if len(answer)==3:
#             return self.question.guess(answer)
#         else:
#             print('need 3 numbers in answer')
#             return (-1, -1)
    
#     def show(self):
#         print(self.question)
    
#     def restart(self):
#         self.__instance = None
#         self.__init__()
    
#     def exit(self):
#         exit()
        

# class MutiGame(Game):
#     def __init__(self, question1:str, question2:str):
#         self.question_for_player1 = NumGroup(question1)
#         self.question_for_player2 = NumGroup(question2)
    
#     def submit(self, answer1, answer2):
#         return (self.question_for_player1.guess(answer1), self.question_for_player2.guess(answer2))

if __name__=='__main__':
    game = SoloGame()
    history = []
    while True:
        a = input('->> ')
        if a=='show':
            game.show()
            continue
        if a=='restart':
            game.restart()
            history = []
            continue
        if a=='exit':
            game.exit()
        h, b = game.submit(a)
        if h==-1 and b==-1:
            continue
        history.append([a, h, b])
        print(f'\t| hit\t| blow')
        for i in history:
            print(f'{i[0]}\t| {i[1]}\t| {i[2]}')
        if h==3:
            print(f'get it in {len(history)} times! Press restart to start new game!')