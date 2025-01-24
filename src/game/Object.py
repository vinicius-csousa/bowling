import pygame

class Object:
    def __init__(self, x: float, y: float, rot_x: float, rot_y: float, scale_x: float, scale_y: float, texture: pygame.Surface):
        self.x = x
        self.y = y
        self.rot_x = rot_x
        self.rot_y = rot_y
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.texture = texture

    def render(self, screen: pygame.Surface) -> None:
        scaled_texture = pygame.transform.scale(
            self.texture,
            (
                self.texture.get_width() * self.scale_x, 
                self.texture.get_height() * self.scale_y
            )
        )
        screen.blit(scaled_texture, (self.x, self.y))

    def get_position(self):
        return (self.x, self.y)