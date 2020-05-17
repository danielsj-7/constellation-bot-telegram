class star_scrapper:
    SIZE = 100
    def __init__(self):
        self.stars_list = self.create_stars_list()

    def coords_to_pixel(self, orig_x, orig_y, size):
        x_pos = size / 2 + (orig_x * size / 2)
        y_pos = size / 2 - (orig_y * size / 2)
        return (x_pos, y_pos)

    def create_all_stars_map(self):
        x = []
        y = []

        for linea in  self.stars_list:
            new_sys = self.coords_to_pixel(float(linea[0]), float(linea[1]), self.SIZE)
            x.append(new_sys[0])
            y.append(new_sys[1])
        return (x, y)

    def create_stars_list(self):
        with open('C:/Users/Daniel/PycharmProjects/bot_constellations/processing/data/stars.txt', 'r') as f:
            str_arr = []
            for  linea in  f.read().splitlines():
                str_arr.append(linea.split(' '))
            return str_arr

