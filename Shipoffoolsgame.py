from random import randint  # importing randint method from random module


class Die:
    
    def __init__(self) -> None:
        
        self._value = 1  # initializing value which is for private use
        self.roll()  # calling roll method of this class.

    def roll(self) -> None:
        
        self._value = randint(1, 6)  # assigns value random number between 1-6

    def get_value(self) -> int:
        return self._value  # returns value


class DiceCup:

    def __init__(self,number: int):
        self._dice=[]
        self._check=[]
        for die in range(number):
            self._check.append(False)
        for die in range(number):
            self._dice.append(Die())

    def roll(self) ->None:
        #This is responsible for rolling all the unbanked Dices
        for roll in range(len(self._check)):
            if self._check[roll]==False:
                self._dice[roll].roll()

    def value(self,index: int) ->int:
        #Returns value of type integer for input1 given _dice index
        return self._dice[index].get_value()

    def bank(self,index: int) ->None:
        #Banks the _dice of given index
        self._check[index]=True

    def is_banked(self,index: int) ->bool:
        #Checks whether the _dice is banked or not for input1 given _dice index
        if self._check[index]==True:
            return True
        else:
            return False

    def release(self,index: int) ->None:
        #Unbanks the _dice of given _dice index
        self._check[index]==False

    def release_all(self) ->None:
        #Unbanks all the dices
        for number in range(5):
            self._check[number]=False
    
    def __str__(self) -> str:
        
        lst = []
        for i in range(len(self._dice)):
            lst.append(str(self.value(i)))  # adds each die value to list
        return " ".join(lst)
        

class ShipOfFoolsGame:
    
    def __init__(self) -> None:
        self.winning_score = 21  # initialises the winning_score
        self._cup = None

    def round(self) -> int:
        
        self._cup = DiceCup(5)  # instantiate object of type DiceCup
        has_ship = False  # initial value of has_ship before starting
        has_captain = False  # initial value of has_captain before starting
        has_crew = False  # initial value of has_crew before starting

        # This will be the sum of the remaining _dice, i.e., the score.
        crew = 0

        # Repeat three times
        for _ in range(3):
            self._cup.roll()  # rolls 5 _dice

            
            if has_ship == False:
                for i in range(len(self._cup._dice)):
                    if not self._cup.is_banked(i):
                        if self._cup.value(i) == 6:
                            self._cup.bank(i)
                            has_ship = True
                            break

           
            # has_captain to True
            if has_ship == True and  has_captain == False:
                # A ship but not a captain is banked
                for i in range(len(self._cup._dice)):
                    if not self._cup.is_banked(i):
                        if self._cup.value(i) == 5:
                            self._cup.bank(i)
                            has_captain = True
                            break

           
            if has_captain == True and  has_crew == False:
                # A ship and captain but not a crew is banked
                for i in range(len(self._cup._dice)):
                    if not self._cup.is_banked(i):
                        if self._cup.value(i) == 4:
                            self._cup.bank(i)
                            has_crew = True
                            break

            if has_ship == True and has_captain == True and has_crew == True:
                # Now we got all needed _dice,can bank the ones we like to save.
                for i in range(len(self._cup._dice)):
                    if not self._cup.is_banked(i):
                        if self._cup.value(i) > 3:
                            self._cup.bank(i)

            print(self._cup)

        # If we have a ship, captain and crew (sum 15),
        # calculate the sum of the two remaining.
        sum = 0  # initial value 0 taken before summing up all the die values
        if has_ship == True and has_captain == True and has_crew == True:
            for i in range(len(self._cup._dice)):
                sum += self._cup.value(i)  # adding die values
            
            crew = sum - 15  # store crew value
        return crew


class PlayerRoom:
   

    def __init__(self) -> None:
       
        self._players = []
        self._game = None
        self.winner = None

    def set_game(self, game: ShipOfFoolsGame) -> None:
        

        self._game = game  # assigns ShipOfFoolsGame

    def add_player(self, player) -> None:
       

        self._players.append(player)  # appending player to players list

    def reset_scores(self) -> None:
        for player in self._players:
            player.reset_score()  # calls reset_score method from Player Class

    # noinspection PyProtectedMember
    def play_round(self) -> None:
        
        for player in self._players:
            player.play_round(self._game)  # calls play_round method of Player Class
            print(f"Above {player._name}'s play in this round")

    def game_finished(self) -> bool:
        
        count = 1  # count holds 1 if no tie

        score = -1  # initial score

        
        for player in self._players:
            if player.current_score() > score:
                score = player.current_score()

        for i in range(len(self._players)):
            current = self._players[i].current_score()  # current player score

            
            for j in range(i + 1, len(self._players)):
                score = self._players[j].current_score()
                if (current == score and current >= 21 and score >= 21 and
                        current == score and score == score):
                    count = 0  # count set to 0 when there is tie
                    break
            # if tie is noticed between the score players,continue playing.
            if count == 0:
                break
        for player in self._players:
            # checking if any player reached winning_score
            if player.current_score() >= 21:
                # count status 0 indicates there is tie so returns false
                if count == 0:
                    print('There is a tie in the match')
                    print('Play another round')
                    return False

                # if count value 1 then no tie so returns True
                else:
                    return True

        # returns False if any player has not reached the winning_score
        return False

    def print_scores(self) -> None:
        
        for player in self._players:
            print(f"{player._name}  current score: {player.current_score()}")

    def print_winner(self) -> None:
       

        score = -1  # initial score

        for player in self._players:
            if player.current_score() > score:
                score = player.current_score()
                self.winner = player._name

        print(f"The winner is {self.winner}")  # prints the winner


class Player:

    def __init__(self,player_name : str):
        self._name = self.set_name(player_name)
        self._score = 0

    def set_name(self,namestring : str) ->str:
        #Returns name of the player
        return namestring

    def current_score(self) ->int:
        #Returns current score of the player
        return self._score

    def reset_score(self) ->None:
        #Sets score of input1 player to 0
        self._score = 0

    def play_round(self, game :ShipOfFoolsGame) ->None:
        #Makes input1 player to play thier round and update thier overall score
        gamer = game
        self._score += gamer.round()

if __name__ == "__main__":
    room = PlayerRoom()  # instantiate the room object of type PlayRoom
    room.set_game(ShipOfFoolsGame())  # room object calls set_game method
    room.add_player(Player("sai"))  # room object calls add_player method
    room.add_player(Player("kumar"))  # room object calls add_player method
    room.reset_scores()  # calls reset_scores method

    # checks if game finished
    while not room.game_finished():
        room.play_round()
        room.print_scores()
    room.print_winner()
