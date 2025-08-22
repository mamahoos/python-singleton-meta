from weakref import WeakKeyDictionary
from typing import Type, Any
from threading import Lock


class SingletonMeta(type):
    _instances  = WeakKeyDictionary()
    _lock: Lock = Lock()
    
    def __call__[T](cls: Type[T], *args: Any, **kwargs: Any) -> T:
        if cls not in SingletonMeta._instances:
            with SingletonMeta._lock:
                if cls not in SingletonMeta._instances:
                    SingletonMeta._instances[cls] = super().__call__(*args, **kwargs)
        return SingletonMeta._instances[cls]
    
    
class Singleton(metaclass=SingletonMeta):
    pass