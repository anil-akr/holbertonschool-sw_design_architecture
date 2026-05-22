#!/usr/bin/env python3
"""
Factory Pattern example.

A factory creates vehicle objects dynamically based on a string key.
New vehicle types can be registered without modifying existing code.
"""

from __future__ import annotations


class Bus:
    """
    Concrete vehicle: Bus.
    """

    def mode(self) -> str:
        """
        Return the transportation mode.
        """
        return "road"


class Train:
    """
    Concrete vehicle: Train.
    """

    def mode(self) -> str:
        """
        Return the transportation mode.
        """
        return "rails"


class Bike:
    """
    Concrete vehicle: Bike.
    """

    def mode(self) -> str:
        """
        Return the transportation mode.
        """
        return "lane"


class Scooter:
    """
    Concrete vehicle: Scooter.
    """

    def mode(self) -> str:
        """
        Return the transportation mode.
        """
        return "scooter_lane"


class VehicleFactory:
    """
    Factory responsible for creating vehicle instances.
    """

    def __init__(self) -> None:
        """
        Initialize the registry with default vehicle types.
        """
        self._registry: dict[str, type] = {
            "bus": Bus,
            "train": Train,
            "bike": Bike,
        }

    def register_kind(self, name: str, cls: type) -> None:
        """
        Register a new vehicle type dynamically.

        Args:
            name: String identifier for the vehicle.
            cls: Vehicle class associated with the identifier.
        """
        self._registry[name] = cls

    def create(self, kind: str) -> object:
        """
        Create and return a vehicle instance.

        Args:
            kind: Vehicle type name.

        Returns:
            A new instance of the requested vehicle.

        Raises:
            ValueError: If the vehicle type is unknown.
        """
        if kind not in self._registry:
            raise ValueError(f"Unknown vehicle kind: {kind!r}")

        return self._registry[kind]()


def main() -> None:
    """
    Demonstrate the Factory pattern.
    """

    # Create factory
    factory = VehicleFactory()

    # Create default vehicle types
    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())

    # Register a new vehicle type dynamically
    factory.register_kind("scooter", Scooter)

    # Create the newly registered vehicle
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
