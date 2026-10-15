from abc import ABC, abstractmethod


class AbstractGakushoku(ABC):
    @abstractmethod
    def get_menu(self) -> str:
        pass

    @abstractmethod
    def get_summary(self) -> str:
        pass

    @abstractmethod
    def get_author(self) -> str:
        pass
