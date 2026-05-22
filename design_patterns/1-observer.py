#!/usr/bin/env python3
"""
Observer Pattern example.

A subject (NewsSubject) keeps track of observers and notifies them
when new information is published.
"""

from __future__ import annotations
from typing import Protocol


class Observer(Protocol):
    """
    Observer interface.

    Any observer must implement update().
    """

    def update(self, topic: str, data: str) -> None:
        ...


class NewsSubject:
    """
    Subject that manages subscriptions and notifications.
    """

    def __init__(self) -> None:
        """
        Store observers with their optional topic interests.

        - key   -> observer instance
        - value -> set of topics OR None for all topics
        """
        self._subs: dict[Observer, set[str] | None] = {}

    def subscribe(
        self,
        observer: Observer,
        topics: set[str] | None = None
    ) -> None:
        """
        Add an observer to the subscription list.

        If topics is None, the observer receives all notifications.
        """
        if observer in self._subs:
            return  # Ignore duplicate subscriptions

        self._subs[observer] = topics

    def unsubscribe(self, observer: Observer) -> None:
        """
        Remove an observer from the subscription list.
        """
        self._subs.pop(observer, None)

    def notify(self, topic: str, data: str) -> None:
        """
        Notify all interested observers about a topic update.
        """
        for observer, interests in list(self._subs.items()):

            # Skip observers not interested in this topic
            if interests is not None and topic not in interests:
                continue

            observer.update(topic, data)


class LogObserver:
    """
    Observer that logs notifications.
    """

    def update(self, topic: str, data: str) -> None:
        """
        Receive notification from subject.
        """
        print(f"log:{topic}={data}")


class EmailObserver:
    """
    Observer that simulates email notifications.
    """

    def update(self, topic: str, data: str) -> None:
        """
        Receive notification from subject.
        """
        print(f"email:{topic}={data}")


class SmsObserver:
    """
    Observer that simulates SMS notifications.
    """

    def update(self, topic: str, data: str) -> None:
        """
        Receive notification from subject.
        """
        print(f"sms:{topic}={data}")


def main() -> None:
    """
    Demonstrate the Observer pattern.
    """

    # Create subject
    subject = NewsSubject()

    # Create observers
    log = LogObserver()
    email = EmailObserver()
    sms = SmsObserver()

    # Subscribe observers with topic filters
    subject.subscribe(log, topics={"sports", "breaking"})
    subject.subscribe(email)  # Receives all topics
    subject.subscribe(sms, topics={"breaking"})

    # Send notifications
    subject.notify("weather", "rain")
    subject.notify("sports", "goal")
    subject.notify("breaking", "alert")


if __name__ == "__main__":
    main()