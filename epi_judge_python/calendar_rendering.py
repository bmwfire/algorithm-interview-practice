import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))


def find_max_simultaneous_events(A):
    E = [p for event in A for p in
         (Endpoint(event.start, True), Endpoint(event.finish, False))]

    E.sort(key=lambda e: (e.time, not e.is_start))

    max_num_simultaneous_events, num_simultaneous_events = 0, 0
    for e in E:
        if e.is_start:
            num_simultaneous_events += 1
            max_num_simultaneous_events = max(max_num_simultaneous_events, num_simultaneous_events)
        else:
            num_simultaneous_events -= 1
    return max_num_simultaneous_events


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(
        functools.partial(find_max_simultaneous_events, events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("calendar_rendering.py",
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
