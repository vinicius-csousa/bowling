from src.game.Object import Object

class Pin(Object):
    @staticmethod
    def get_positions(screen_width: int, screen_height: int, pin_width: int) -> list[tuple[float, float]]:
        lane_start = 331 / 720
        lane_end = 395 / 720
        
        interval = (lane_end - lane_start) / 4
        layer4 = [(screen_width * x - pin_width / 2, screen_height * 0.125) for x in [lane_start + interval / 2, lane_start + interval * 1.5, lane_end - interval * 1.5, lane_end - interval / 2]]

        interval = (lane_end - lane_start) / 2
        layer3 = [(screen_width * x - pin_width / 2, screen_height * 0.150) for x in [lane_start + interval / 2, lane_start + interval * 1, lane_end - interval / 2]]

        interval = (lane_end - lane_start) / 2 
        layer2 = [(screen_width * x - pin_width / 2, screen_height * 0.175) for x in [lane_start + interval * 0.75, lane_end - interval * 0.75]]


        layer1 = [(screen_width * 0.5 - pin_width / 2, screen_height * 0.2)]

        return layer4 + layer3 + layer2 + layer1
