class star_scrapper:
    def __init__(self):
        self.stars_list = self.create_stars_list()


    def create_dot_map(self):
        dot_map = []
        for line in self.stars_list:
            
            pass

    def create_stars_list(self):
        with open('C:/Users/Daniel/PycharmProjects/bot_constellations/processing/data/stars.txt', 'r') as f:
            return f.read().splitlines()