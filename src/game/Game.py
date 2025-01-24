import pygame
from src.score.BowlingManager import BowlingManager
from src.game.Renderer import Renderer
from src.game.Object import Object
from src.game.Ball import Ball
from src.game.Pin import Pin
from src.game.enums.Status import Status

class Game:
    def __init__(self, screen_size: tuple[int, int]):
        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode(screen_size)
        self.renderer: Renderer = Renderer()
        self.lane: Object
        self.ball: Ball
        self.pins: list[Pin]
        self.play_button: Object
        self.running: bool = False
        self.manager: BowlingManager
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.dt: float = 0.1
        self.game_status: Status = Status.NOT_STARTED
        self.__create_objects()

    def run(self):
        self.running = True 
        while self.running:
            self.__poll_events()
            self.__update()
            self.renderer.render(
                self.screen,
                [self.lane, self.ball, *self.pins]
            )

            self.dt = self.clock.tick(60) / 1000
            self.dt = max(0.001, min(0.1, self.dt))

        pygame.quit()

    def __create_objects(self) -> None:
        assets = self.renderer.get_assets()
        lane = assets["lane"]
        ball = assets["ball"]
        pin = assets["pin"]
        play_button = assets["dc_logo"]

        self.lane = Object(0, 0, 0, 0, 1, 1, lane)
        self.ball = Ball(self.screen.width / 2, self.screen.height * 0.65, 0, 0, 0.2, 0.2, ball)
        self.pins = [
            Pin(pos[0], pos[1], 0, 0, 0.15, 0.15, pin) 
            for pos in Pin.get_positions(self.screen.width, self.screen.height, pin.width*0.15)
            ]

    def __poll_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.__play()

    def __update(self) -> None:
        if self.game_status == Status.ROLLLING:
            self.ball.move(-300 * self.dt, 0.99)

        if self.ball.get_position()[1] < self.screen.height * 0.15:
            self.game_status = Status.STANDBY
            self.ball.reset(self.screen.width, self.screen.height)

    def __play(self) -> None:
        if self.game_status in [Status.NOT_STARTED, Status.STANDBY]:        
            self.game_status = Status.ROLLLING
            self.ball.move(-300 * self.dt, 0.99)

                