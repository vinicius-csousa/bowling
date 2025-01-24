import pygame
from src.game.Object import Object
from pathlib import Path

class Renderer:
    def __init__(self):
        self.assets: dict[str, pygame.Surface] = self.__load_assets()

    def __load_assets(self) -> dict[str, pygame.Surface]:
        images_path = Path(__file__).absolute().parent.parent.parent / "images"
        return {
            Path(filename).stem: pygame.image.load(filename).convert_alpha() for filename in Path(images_path).glob("*")
        }
    
    def get_assets(self) -> dict[str, pygame.Surface]:
        return self.assets

    def render(self, screen: pygame.Surface, objects: list[Object]):
        for object in objects:
            object.render(screen)

        pygame.display.flip()