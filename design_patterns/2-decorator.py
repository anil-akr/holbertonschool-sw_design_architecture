#!/usr/bin/python3

class Beverage:
    """Base beverage class."""

    def cost(self):
        raise NotImplementedError

    def description(self):
        raise NotImplementedError


class Coffee(Beverage):
    """Concrete beverage."""

    def cost(self):
        return 50

    def description(self):
        return "Coffee"


class MilkDecorator(Beverage):
    """Decorator that adds milk."""

    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 10

    def description(self):
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    """Decorator that adds sugar."""

    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 5

    def description(self):
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    """Decorator that adds caramel."""

    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 15

    def description(self):
        return self._inner.description() + " + caramel"


if __name__ == "__main__":
    coffee = MilkDecorator(Coffee())
    print(coffee.description(), coffee.cost())

    coffee2 = MilkDecorator(SugarDecorator(Coffee()))
    print(coffee2.description(), coffee2.cost())

    coffee3 = CaramelDecorator(
        MilkDecorator(
            SugarDecorator(
                Coffee()
            )
        )
    )
    print(coffee3.description(), coffee3.cost())
