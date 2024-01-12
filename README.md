This example uses the `PrefectCloudEventSubscriber` to block execution of a flow until a set of event names are seen, providing `AND` behavior. A parent flow runs groups of deployments, waiting until all desired event names are seen before proceeding to trigger each group of deployment runs.

Though this example is only looking for events emitted by the flows it's running, it could potentially listen for events from any source.

[flow run graph](/listener-orchestrator.png)
