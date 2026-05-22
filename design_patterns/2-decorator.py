#!/usr/bin/env python3
"""
Decorator Pattern example.

Decorators allow adding optional behavior dynamically
without creating many subclasses.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Beverage(ABC):
    """
    Abstract base class for all beverages.
    """

    @abstractmethod
    def cost(self) -> int:
        """
        Return the beverage cost in cents.
        """
        ...

    @abstractmethod
    def description(self) -> str:
        """
        Return the beverage description.
        """
        ...


class Coffee(Beverage):
    """
    Concrete beverage implementation.
    """

    def cost(self) -> int:
        """
        Base coffee costs 50 cents.
        """
        return 50

    def description(self) -> str:
        """
        Return beverage name.
        """
        return "Coffee"


class MilkDecorator(Beverage):
    """
    Decorator that adds milk to a beverage.
    """

    def __init__(self, inner: Beverage) -> None:
        """
        Wrap another beverage object.
        """
        self._inner = inner

    def cost(self) -> int:
        """
        Add 10 cents to the wrapped beverage cost.
        """
        return self._inner.cost() + 10

    def description(self) -> str:
        """
        Add milk to the beverage description.
        """
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    """
    Decorator that adds sugar to a beverage.
    """

    def __init__(self, inner: Beverage) -> None:
        """
        Wrap another beverage object.
        """
        self._inner = inner

    def cost(self) -> int:
        """
        Add 5 cents to the wrapped beverage cost.
        """
        return self._inner.cost() + 5

    def description(self) -> str:
        """
        Add sugar to the beverage description.
        """
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    """
    Decorator that adds caramel to a beverage.
    """

    def __init__(self, inner: Beverage) -> None:
        """
        Wrap another beverage object.
        """
        self._inner = inner

    def cost(self) -> int:
        """
        Add 15 cents to the wrapped beverage cost.
        """
        return self._inner.cost() + 15

    def description(self) -> str:
        """
        Add caramel to the beverage description.
        """
        return self._inner.description() + " + caramel"


def main() -> None:
    """
    Demonstrate the Decorator pattern.
    """

    # Coffee with milk
    cup1 = MilkDecorator(Coffee())
    print(cup1.description(), cup1.cost())

    # Coffee with sugar and milk
    cup2 = MilkDecorator(SugarDecorator(Coffee()))
    print(cup2.description(), cup2.cost())

    # Coffee with sugar, milk, and caramel
    cup3 = CaramelDecorator(
        MilkDecorator(
            SugarDecorator(
                Coffee()
            )
        )
    )

    print(cup3.description(), cup3.cost())


if __name__ == "__main__":
    main()
