from prefect import flow, task, get_run_logger
from prefect.events import emit_event


@flow
def child(events_to_emit: list[str] | None = None):
    if events_to_emit:
        [emit(event) for event in events_to_emit]

    else:
        get_run_logger().info("No events to emit")


@task
def emit(event: str):
    get_run_logger().info(f"Emitting event {event!r}")
    emit_event(event, resource={"prefect.resource.id": "custom-events.event"})
