# listener-orchestrator

This example uses the `PrefectCloudEventSubscriber` to block execution of a flow until a set of event names are seen, providing `AND` behavior. A parent flow waits until all desired event names are seen before proceeding to trigger each downstream group of child deployments.

## Running the example

Ensure you are in a python environment with `prefect` installed.
Run `python deployment.py` to serve the parent and child deployments.
Then, in a separate terminal, run `prefect deployment run parent/parent` to execute the parent deployment.

![flow run graph](/listener-orchestrator.png)
Note that in this image, the child deployments are submitted before the event listener begins, but appear slightly delayed because of their momentary scheduled/pending states.

Though this example is only looking for events emitted by the flows it's running, it could potentially listen for events from any source.
