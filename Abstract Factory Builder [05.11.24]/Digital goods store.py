from abc import ABC, abstractmethod

# Абстрактные продукты
class Game(ABC):
    @abstractmethod
    def get_details(self) -> str:
        pass

    @abstractmethod
    def download(self) -> str:
        pass

    @abstractmethod
    def play(self) -> str:
        pass


class Music(ABC):
    @abstractmethod
    def get_details(self) -> str:
        pass

    @abstractmethod
    def download(self) -> str:
        pass

    @abstractmethod
    def play(self) -> str:
        pass

# Конкретные продукты для Game
class ActionGame(Game):
    def get_details(self) -> str:
        return 'Action Game: Dynamic and addictive game'

    def download(self) -> str:
        return 'Downloading Action Game'

    def play(self) -> str:
        return 'Starting Action Game'


class PuzzleGame(Game):
    def get_details(self) -> str:
        return 'Puzzle Game: Fascinating puzzle for the mind'

    def download(self) -> str:
        return 'Downloading Puzzle Game'

    def play(self) -> str:
        return 'Starting Puzzle Game'

# Конкретные продукты для Music
class RockMusic(Music):
    def get_details(self) -> str:
        return 'Rock Music: Energetic rock compositions'

    def download(self) -> str:
        return 'Downloading Rock Music'

    def play(self) -> str:
        return 'Playing Rock Music'


class JazzMusic(Music):
    def get_details(self) -> str:
        return 'Jazz Music: Calm jazz melodies'

    def download(self) -> str:
        return 'Downloading Jazz Music'

    def play(self) -> str:
        return 'Playing Jazz Music'

# Абстрактная фабрика
class DigitalProductFactory(ABC):
    @abstractmethod
    def create_game(self) -> Game:
        pass

    @abstractmethod
    def create_music(self) -> Music:
        pass

# Конкретные фабрики
class EntertainmentFactory(DigitalProductFactory):
    def create_game(self) -> Game:
        return ActionGame()

    def create_music(self) -> Music:
        return RockMusic()


class PuzzleFactory(DigitalProductFactory):
    def create_game(self) -> Game:
        return PuzzleGame()

    def create_music(self) -> Music:
        return JazzMusic()

# Клиентский код
def main(factory: DigitalProductFactory):
    game = factory.create_game()
    music = factory.create_music()

    products = [game, music]

    for item in products:
        print(item.get_details())
        print(item.download())
        print(item.play())
        print('-' * 40)

if __name__ == "__main__":
    print('Using EntertainmentFactory:')
    entertainment_factory = EntertainmentFactory()
    main(entertainment_factory)

    print('\nUsing PuzzleFactory:')
    puzzle_factory = PuzzleFactory()
    main(puzzle_factory)