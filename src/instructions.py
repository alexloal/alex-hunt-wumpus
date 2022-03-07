class Instructions:

    @staticmethod
    def show_header():
        print("""
,--.  ,--.                     ,--.     ,--------. ,--.                ,--.   ,--.                                              
|  '--'  | ,--.,--. ,--,--,  ,-'  '-.   '--.  .--' |  ,---.   ,---.    |  |   |  | ,--.,--. ,--,--,--.  ,---.  ,--.,--.  ,---.  
|  .--.  | |  ||  | |      \ '-.  .-'      |  |    |  .-.  | | .-. :   |  |.'.|  | |  ||  | |        | | .-. | |  ||  | (  .-'  
|  |  |  | '  ''  ' |  ||  |   |  |        |  |    |  | |  | \   --.   |   ,'.   | '  ''  ' |  |  |  | | '-' ' '  ''  ' .-'  `) 
`--'  `--'  `----'  `--''--'   `--'        `--'    `--' `--'  `----'   '--'   '--'  `----'  `--`--`--' |  |-'   `----'  `----'  
        """)

    @staticmethod
    def show_game_over():
        print("""
         ,----.      ,---.   ,--.   ,--. ,------.    ,-----.  ,--.   ,--. ,------. ,------.  
        '  .-./     /  O  \  |   `.'   | |  .---'   '  .-.  '  \  `.'  /  |  .---' |  .--. ' 
        |  | .---. |  .-.  | |  |'.'|  | |  `--,    |  | |  |   \     /   |  `--,  |  '--'.' 
        '  '--'  | |  | |  | |  |   |  | |  `---.   '  '-'  '    \   /    |  `---. |  |\  \  
         `------'  `--' `--' `--'   `--' `------'    `-----'      `-'     `------' `--' '--' 
         """)

    @staticmethod
    def show_instructions():
        print("""
            THE WUMPUS LIVES IN A CAVE OF 20 ROOMS.
            EACH ROOM HAS 3 TUNNELS LEADING TO OTHER ROOMS.
            
        HAZARDS:
            -BOTTOMLESS PITS-: TWO ROOMS HAVE BOTTOMLESS PITS IN THEM. IF YOU GO THERE, YOU FALL INTO THE PIT & LOSE.
            -SUPER BATS-: TWO OTHER ROOMS HAVE SUPER BATS. IF YOU GO THERE, A BAT GRABS YOU AND TAKES YOU TO SOME OTHER ROOM.
        
        WUMPUS:
            -THE WUMPUS IS NOT BOTHERED BY THE HAZARDS. 
            -USUALLY HE IS ASLEEP. 
            -TWO THINGS THAT WAKE HIM UP: YOUR ENTERING HIS ROOM OR YOUR SHOOTING AN ARROW. 
            -IF THE WUMPUS WAKES, HE MOVES (P=.75) ONE ROOM OR STAYS STILL (P=.25). 
            -AFTER THAT, IF HE IS WHERE YOU ARE, HE TRAMPLES YOU & YOU LOSE!.
            
        YOU:
            -EACH TURN YOU MAY MOVE OR SHOOT AN ARROW.
            -MOVING: YOU CAN GO ONE ROOM.
            -ARROWS: YOU HAVE 5 ARROWS. 
            -YOU LOSE WHEN YOU RUN OUT. 
            -YOU AIM BY TELLING THE COMPUTER THE ROOM YOU WANT THE ARROW TO GO TO.
            -IF THE ARROW HITS THE WUMPUS, YOU WIN.
            
        WARNINGS:
            -WHEN YOU ARE ONE ROOM AWAY FROM WUMPUS OR A HAZARD,
            -THE COMPUTER SAYS:
                -WUMPUS:   'I SMELL A WUMPUS'
                -BAT   :   'BATS NEAR BY'
                -PIT   :   'I FEEL A DRAFT'
        
        GAME OPTIONS:
            -HARD: 2 BATS, 5 PITS, 1 WUMPUS WITH ONLY 3 ARROWS 
            -NORMAL: 2 BATS, 2 PITS AND 1 WUMPUS
            -EASY: 1 BAT, 1 PIT AND 1 WUMPUS
        
        
        """)

    @staticmethod
    def print_score_list(info):
        print()
        print("""
         ,---.                                  
        '   .-'   ,---.  ,---.  ,--.--.  ,---.  
        `.  `-.  | .--' | .-. | |  .--' | .-. : 
        .-'    | \ `--. ' '-' ' |  |    \   --. 
        `-----'   `---'  `---'  `--'     `----' 
        """)
        for line in info:
            words = line.split('#')
            name = words[0]
            score = words[1].replace('\n', '')
            print('{:<20}{:>20}'.format(name, score))
