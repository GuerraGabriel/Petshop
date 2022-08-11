from src.UseCase.UseCaseInterface import UseCaseInterface

class RouterInterface:
    service: UseCaseInterface
    
    def __init__(self, service: UseCaseInterface) -> None:
        raise NotImplementedError()
    
    def handle(self, request):
        raise NotImplementedError()