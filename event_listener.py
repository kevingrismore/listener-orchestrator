from typing import Callable

from websockets.exceptions import ConnectionClosedError

from prefect.events.clients import PrefectCloudEventSubscriber
from prefect.events.filters import EventFilter
from prefect.logging.loggers import get_logger

logger = get_logger("event.listener")


async def listen_for_events_until(
    event_filter: EventFilter, until: Callable[..., bool]
):
    """Listen for events until the provided function returns True."""
    seen_events = set()
    filtered_events = set(event_filter.event.name)
    while True:
        try:
            async with PrefectCloudEventSubscriber(filter=event_filter) as subscriber:
                async for event in subscriber:
                    logger.info(f"📬 Received event {event.event!r}")
                    seen_events.add(event.event)

                    if until(seen_events, filtered_events):
                        return

        except ConnectionClosedError:
            logger.debug("🚨 Connection closed, reconnecting...", "red")
