from abc import ABC, abstractmethod

# Интерфейсы для классов Game и Music
class Detailed(ABC):
    @abstractmethod
    def get_details(self):
        pass

class Downloadable(ABC):
    @abstractmethod
    def download(self):
        pass

class Playable(ABC):
    @abstractmethod
    def play(self):
        pass


# Абстрактные классы продуктов
class Game(Detailed, Downloadable, Playable):
    pass

class Music(Detailed, Downloadable, Playable):
    pass


# Конкретные классы для игр
class ActionGame(Game):
    def get_details(self):
        print('Action Game: Dynamic and addictive game')

    def download(self):
        print('Downloading Action Game')

    def play(self):
        print('Starting Action Game')

class PuzzleGame(Game):
    def get_details(self):
        print('Pazzle Game: Fascinating puzzle for the mind')

    def download(self):
        print('Downloading Pazzle Game')

    def play(self):
        print('Starting Pazzle Game')

# Конкретные классы длля музыки
class RockMusic(Music):
    def get_details(self):
        print('Rock Music: Energetic rock compositions')

    def download(self):
        print('Downloading Rock Music')

    def play(self):
        print('Playing Rock Music')

class JazzMusic(Music):
    def get_details(self):
        print('Jazz Music: Calm jazz melodies')

    def download(self):
        print('Downloading Jazz Music')

    def play(self):
        print('Playing Jazz Music')


# Абстрактная фабрика для игр
class GameFactory(ABC):
    @abstractmethod
    def create_game(self) -> Game:
        pass

# Абстрактная фабрика для музыки
class MusicFactory(ABC):
    @abstractmethod
    def create_music(self) -> Music:
        pass


# Конкретные фабрики для игр
class ActionGameFactory(GameFactory):
    def create_game(self) -> Game:
        return ActionGame()

class PuzzleGameFactory(GameFactory):
    def create_game(self) -> Game:
        return PuzzleGame()

# Конкретные фабрики для музыки
class RockMusicFactory(MusicFactory):
    def create_music(self) -> Music:
        return RockMusic()

class JazzMusicFactory(MusicFactory):
    def create_music(self) -> Music:
        return JazzMusic()


# Абстрактная фабрика, которая определяет методы для получения фабрик типов продуктов
class DigitalProductFactory(ABC):
    @abstractmethod
    def get_game_factory(self) -> GameFactory:
        pass

    @abstractmethod
    def get_music_factory(self) -> MusicFactory:
        pass


# Конкретная фабрика развлечений, создающая ActionGame и RockMusic
class EntertainmentFactory(DigitalProductFactory):
    def get_game_factory(self) -> GameFactory:
        return ActionGameFactory()

    def get_music_factory(self) -> MusicFactory:
        return RockMusicFactory()

# Конкретная фабрика головоломок, создающая PuzzleGame и JazzMusic
class PuzzleFactory(DigitalProductFactory):
    def get_game_factory(self) -> GameFactory:
        return PuzzleGameFactory()

    def get_music_factory(self) -> MusicFactory:
        return JazzMusicFactory()


def main(factory: DigitalProductFactory):
    game_factory = factory.get_game_factory()
    music_factory = factory.get_music_factory()

    game = game_factory.create_game()
    music = music_factory.create_music()

    products = [game, music]

    for item in products:
        item.get_details()
        item.download()
        item.play()
        print('-' * 40)


print('Using EntertainmentFactory:')
entertainment_factory = EntertainmentFactory()
main(entertainment_factory)

print('\nUsing PuzzleFactory:')
puzzle_factory = PuzzleFactory()
main(puzzle_factory)