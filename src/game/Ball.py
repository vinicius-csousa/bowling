from src.game.Object import Object
import pygame

class Ball(Object):
    def __init__(self, x: float, y: float, rot_x: float, rot_y: float, scale_x: float, scale_y: float, texture: pygame.Surface):
        self.is_moving = False

        super().__init__(x, y, rot_x, rot_y, scale_x, scale_y, texture)

    def move(self, dy: float, scale_factor: float):
        self.y += dy
        self.scale_x, self.scale_y = self.scale_x * scale_factor, self.scale_y * scale_factor

    def render(self, screen: pygame.Surface) -> None:
        scaled_texture = pygame.transform.scale(
            self.texture,
            (
                self.texture.get_width() * self.scale_x, 
                self.texture.get_height() * self.scale_y
            )
        )
        screen.blit(scaled_texture, (self.x - self.texture.width * self.scale_x / 2, self.y - self.texture.width * self.scale_x / 2))

    def reset(self, screen_width: int, screen_height: int):
        self.rot_x, self.rot_y = 0, 0
        self.scale_x, self.scale_y = 0.2, 0.2
        self.x = screen_width / 2
        self.y = screen_height * 0.65
