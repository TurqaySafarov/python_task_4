class Chess:
    def __init__(self, color):
        self.color = color
    
    def move(self):
        pass
    
    def step(self):
        print("1")

class Piyada(Chess):
    def __init__(self, color, starting_square):
        super().__init__(color)
        self.starting_square = starting_square
    
    def move(self):
        print("Piyadalar ancaq qabağa hərəkət edə bilərlər.")

class Fil(Chess):
    def __init__(self, color):
        super().__init__(color)
        print("Addim sayi sonsuz")
    
    def move(self):
        print("Fil ancaq diaqonal xanalarla hərəkət edir")

class At(Piyada):
    def move(self):
        print("At L istiqametde hereket edir.")

class Top(Chess):
    def move(self):
        print("Top şaquli və üfüqi xanalar üzrə hərəkət edir")

class Vezir(Chess):
    def move(self):
        print("Vezir şaquli, üfüqi və ya diaqonal xanalar üzrə hərəkət edir.")

class Sah(Chess):
    def move(self):
        print("Sah öz xanasından rəqib fiqurunun zərbəsi altında olmayan başqa qarışıq xanaya hərəkət edir.")

class ChessGame:
    def __init__(self, history, world_champions):
        self.history = history
        self.world_champions = world_champions

    def display_history(self):
        print("Chess History:", self.history)

    def display_world_champions(self):
        print("World Chess Champions:")
        for champion in self.world_champions:
            print(champion)

history = "VI esr Hindistan"
world_champions = ["Wilhelm Steinitz", "Emanuel Lasker", "José Raúl Capablanca",
                   "Alexander Alekhine", "Max Euwe", "Mikhail Botvinnik", "Vasily Smyslov",
                   "Mikhail Tal", "Tigran Petrosian", "Boris Spassky", "Bobby Fischer",
                   "Anatoly Karpov", "Garry Kasparov", "Vladimir Kramnik", "Viswanathan Anand",
                   "Magnus Carlsen"]


chess_game = ChessGame(history, world_champions)
chess_game.display_history()
chess_game.display_world_champions()


piyada = Piyada("ağ", "a2")
print("Ağ piyada mövqesi:", piyada.starting_square)

