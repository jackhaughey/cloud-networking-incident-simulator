# Architecture

- **FRR routers (r1, r2, r3)** simulate core, edge, and service networks.
- **VPN** provides remote-access style connectivity into the edge network.
- **LB (nginx)** fronts two stateless app services.
- **App services** represent customer-facing workloads.

The topology is designed to expose:

- BGP routing behaviour and failure modes.
- Load balancing and health-check issues.
- Linux system resource constraints (disk, memory, logs).
