from prefect import flow, task, get_run_logger
from prefect.deployments.deployments import run_deployment
from prefect.events.filters import EventFilter

from event_listener import listen_for_events_until as listen


@flow
def parent():
    for deployment in ["child/child-1", "child/child-2"]:
        run_deployment(name=deployment, timeout=0)

    listen_for_events(["event-1", "event-2"])

    run_deployment(name="child/child-3", timeout=0)

    listen_for_events(["event-3", "event-4"])

    for deployment in ["child/child-4", "child/child-5"]:
        run_deployment(name=deployment, timeout=0)


@task
async def listen_for_events(events: list[str]):
    """Block until all desired events are seen."""
    get_run_logger().info(f"Listening for events {events!r}")
    await listen(
        event_filter=EventFilter(event=dict(name=events)),
        until=all_events_seen,
    )


def all_events_seen(seen_events: set, filtered_events: set):
    """Unblocks the event listener when true."""
    return seen_events.issuperset(filtered_events)


if __name__ == "__main__":
    parent()
