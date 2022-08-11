from src.Repositories import RepositoryInterface

class UseCaseInterface:
    def __init__(self, repository: RepositoryInterface):
        raise NotImplementedError()
    
    def create(self, instance):
        raise NotImplementedError()
    
    def retrieve(self, id):
        raise NotImplementedError()
    
    def update(self):
        raise NotImplementedError()
    
    def delete(self): 
        raise NotImplementedError()