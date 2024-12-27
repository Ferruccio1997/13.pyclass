from abc import ABC, abstractmethod


class AbstractDataSource(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def start(self):
        raise NotImplementedError('Metodo nao implementado')
    
    @abstractmethod
    def get_data(self):
        raise NotImplementedError('Metodo nao implementado')
    
    @abstractmethod
    def transform_data_to_df(self):
        raise NotImplementedError('Metodo nao implementado')
    
    @abstractmethod
    def save_data(self):
        raise NotImplementedError('Metodo nao implementado')
    
    def hello_world(self):
        print('Hello world')