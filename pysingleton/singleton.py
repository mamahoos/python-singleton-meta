from threading import Lock
from typing import Dict, Type, Any


class SingletonMeta(type):
    __instances: Dict[Type[Any], Any] = {}
    
    __lock: Lock = Lock()
    
    def __call__[T](cls: Type[T], *args: Any, **kwargs: Any) -> T:
        with SingletonMeta.__lock:
            if cls not in SingletonMeta.__instances:
                instance = super().__call__(*args, **kwargs)
                SingletonMeta.__instances[cls] = instance
        return SingletonMeta.__instances[cls]
    
    
class Singleton(metaclass=SingletonMeta):
    pass