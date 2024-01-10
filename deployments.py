from prefect import serve

from parent import parent
from child import child

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
