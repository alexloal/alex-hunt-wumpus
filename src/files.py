class Files:

    @staticmethod
    def read_file():
        file = open('data.txt', 'r')
        info = file.readlines()
        file.close()
        return info

    @staticmethod
    def save_new_score(player_name, score):
        file = open('data.txt', 'a')
        file.writelines([player_name, '#', str(score), '\n'])
        file.close()
        return Files().read_file()
