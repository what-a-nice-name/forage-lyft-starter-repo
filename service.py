from abc import ABC, abstractmethod


class Servicebale(ABC):
    @abstractmethod
    def needs_service(self):
        pass
