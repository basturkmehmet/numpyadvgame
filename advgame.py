import random
import numpy as np
class AdvGame():
    def __init__(self, movekey, points, potions, swords, treasures,
                 env_treasure, env_potion,env_sword,env_monster,env_venom,env_empty,
                 place_now, place_after):
        self.movekey=movekey
        self.points=points
        self.potions=potions
        self.swords=swords
        self.treasures=treasures


        self.env_treasure = env_treasure
        self.env_potion = env_potion
        self.env_sword = env_sword
        self.env_monster = env_monster
        self.env_venom = env_venom
        self.env_empty = env_empty

        self.place_now = place_now
        self.place_after = place_after
    def environment(self):
        empty_array = np.full((6, 7), ".")
        self.empty_array=empty_array
        #print(empty_array)
        #print("\033[H\033[J", end="")
        #arylist=["T","T","P"*2]
        #print(arylist)
        #actual_array = np.full((42), " ")
        n=0
        #print(self.env_treasure[n])
        #self.env_treasure=self.env_treasure()

        actual_array=[]

        for items in self.env_treasure:
            actual_array.append(self.env_treasure[n])
        for items in self.env_empty:
            actual_array.append((self.env_empty[n]))
        for items in self.env_venom:
            actual_array.append(self.env_venom[n])
        for items in self.env_sword:
            actual_array.append((self.env_sword[n]))
        for items in self.env_monster:
            actual_array.append(self.env_monster[n])

        #print(actual_array)

        #actual_array=actual_array.ravel()

        self.actual_array01 = random.sample(actual_array,len(actual_array))
        actual_array02=np.reshape(self.actual_array01,(6,7))
        self.actual_array02=actual_array02
        #print(actual_array02)
    def initial(self):
        #print(len(self.actual_array01))
        #self.initial_point_index=random.randrange(len(self.actual_array01))
        #print(self.initial_point_index)
        for items in self.actual_array01:
            random01=random.randint(0,42)
            #print(random01)
            if self.actual_array01[random01]=="E":
                self.initial_point_index=random01
                #print(self.initial_point_index)
                break
            else:
                continue
        self.empty_array=self.empty_array.ravel()
        self.empty_list=list(self.empty_array)
        self.empty_list.insert(self.initial_point_index, "E")
        self.empty_list.pop(self.initial_point_index+1)
        #print(self.empty_list)
        self.empty_array=tuple(self.empty_list)
        #print(len(self.empty_array))
        self.empty_array=np.reshape(self.empty_array, (6,7))
        print(self.empty_array)
    def movement(self):
        if self.movekey=="W":


            if self.place_now==self.place_after:
                self.place_after = self.place_now - 7
                self.empty_array = self.empty_array.ravel()
                self.empty_list = list(self.empty_array)
                self.place_after_ele = self.actual_array01[self.place_after]

                self.empty_list.insert(self.place_after, self.place_after_ele)
                self.empty_list.pop(self.place_after + 1)
                self.empty_array = tuple(self.empty_list)
                self.empty_array = np.reshape(self.empty_array, (6, 7))

                print(self.empty_array)

                self.place_now = self.place_after

            else:
                self.place_now = self.initial_point_index

                self.place_after=self.place_now-7
                self.empty_array = self.empty_array.ravel()
                self.empty_list = list(self.empty_array)
                self.place_after_ele=self.actual_array01[self.place_after]

                self.empty_list.insert(self.place_after, self.place_after_ele)
                self.empty_list.pop(self.place_after + 1)
                self.empty_array = tuple(self.empty_list)
                self.empty_array = np.reshape(self.empty_array, (6, 7))

                print(self.empty_array)

                self.place_now=self.place_after



        else:
            print("Press W")

        #elif self.movekey=="A":
        #elif self.movekey=="S":
        #elif self.movekey=="D":
    ''''
    def runner(self):
        while True:
            self.movekey= input("W A S D:")
            print(self.movekey)

            game1.movement()
'''
m=""


game1 = AdvGame(m,2,3,4,5,["T"]*5,["P"]* 3,["S"]*2,["M"]*5,["V"]*3,["E"]*27,0,0)
game1.environment()
game1.initial()
game1.runner()


