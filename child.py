from prefect import flow, task, serve, get_run_logger
from prefect.events import emit_event
from parent import parent


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


if __name__ == "__main__":
    child_1 = child.to_deployment(
        name="child-1",
        parameters=dict(events_to_emit=["event-1"]),
    )
    child_2 = child.to_deployment(
        name="child-2",
        parameters=dict(events_to_emit=["event-2"]),
    )
    child_3 = child.to_deployment(
        name="child-3",
        parameters=dict(events_to_emit=["event-3", "event-4"]),
    )
    child_4 = child.to_deployment(name="child-4")
    child_5 = child.to_deployment(name="child-5")

    parent_flow = parent.to_deployment(
        name="parent",
    )

    serve(child_1, child_2, child_3, child_4, child_5, parent_flow)
