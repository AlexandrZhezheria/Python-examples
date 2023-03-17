# У нас в Mate Academy працює Alex, який ну дуже любить сендвічі з шинкою.
# Давай допоможемо йому зробити такий сендвіч за допомогою декораторів, розташувавши їх у правильній послідовності.
# Найголовніше — не забудь додати до функції sandwich шинку :), інакше Alex залишиться голодним :(
# Hint: Не забудь ввести три пробіли перед шинкою


from functools import wraps
from typing import Callable, Any


def bread(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print("</--------\\>")
        func(*args, **kwargs)
        print("<\\________/>")

    return wrapper


def ingredients(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(" #tomatoes#")
        func(*args, **kwargs)
        print("   ~salad~")

    return wrapper


@bread
@ingredients
def sandwich() -> None:
    print("   --ham--")


sandwich()

# Приклад:
# sandwich()
# </--------\>
#  #tomatoes#
#    --ham--
#    ~salad~
# <\________/>