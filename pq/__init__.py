import heapq
import itertools
import threading
from typing import Any


class PriorityQueue:
    REMOVED = object()

    def __init__(self):
        self._pq = []
        self._entry_finder = {}
        self._counter = itertools.count()

    def add(self, item: Any, priority: int = 0):
        if item in self._entry_finder:
            self._remove(item)

        count = next(self._counter)
        entry = [priority, count, item]
        self._entry_finder[item] = entry
        heapq.heappush(self._pq, entry)

    def _remove(self, item: Any):
        entry = self._entry_finder.pop(item)
        entry[-1] = PriorityQueue.REMOVED

    def remove(self, item: Any):
        self._remove(item)

    def pop(self) -> Any:
        while self._pq:
            priority, count, item = heapq.heappop(self._pq)
            if item is not PriorityQueue.REMOVED:
                del self._entry_finder[item]
                return item

        raise KeyError('pop from empty priority queue')

    def __len__(self):
        return len(self._entry_finder)


class SafePriorityQueue(PriorityQueue):
    def __init__(self):
        super().__init__()
        self._mux = threading.Lock()

    def add(self, item: Any, priority: int = 0):
        with self._mux:
            super().add(item, priority)

    def remove(self, item: Any):
        with self._mux:
            super().remove(item)

    def pop(self) -> Any:
        with self._mux:
            return super().pop()
