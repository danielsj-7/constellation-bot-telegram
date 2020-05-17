class star_scrapper:
    SIZE = 100
    def __init__(self):
        self.stars_list = self.create_stars_list()

    def coords_to_pixel(self, orig_x, orig_y, size):
        # todo el centro de la imagen y añado el correspondiente offset
        x_pos = size / 2 + (orig_x * size / 2)
        y_pos = size / 2 - (orig_y * size / 2)
        return (x_pos, y_pos)

    def create_dot_map(self):
        x = []
        y = []
        for linea in  self.stars_list:
            lineaP = linea.split(' ')
            print(lineaP)
            new_sys = self.coords_to_pixel(float(lineaP[0]), float(lineaP[1]), self.SIZE)
            x.append(new_sys[0])
            y.append(new_sys[1])
        return (x, y)

    def create_stars_list(self):
        with open('C:/Users/Daniel/PycharmProjects/bot_constellations/processing/data/stars.txt', 'r') as f:
            return f.read().splitlines()

