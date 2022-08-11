

class RepositoryInterface:
    def create(self, instance):
        raise NotImplementedError()
    
    def retrieve(self, id):
        raise NotImplementedError()
    
    def update(self):
        raise NotImplementedError()
    
    def delete(self): 
        raise NotImplementedError()