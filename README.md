# Cloud Networking Incident Simulator & Runbook Automation

This repository provides a reproducible lab that simulates real-world
Severity 1/2 incidents in a cloud networking environment:

- BGP route distribution and failure modes
- Load balancer and health-check misconfiguration
- VPN tunnel instability
- Linux system failures (disk full, log growth, process crashes)

## Purpose

This lab is part of my ongoing effort to deepen and polish two core skill areas essential for cloud networking operations:

- **BGP routing expertise** — building, breaking, and repairing realistic multi‑router topologies using FRRouting, including route flaps, misconfigurations, and convergence analysis.
- **Python automation** — developing tooling for log analysis, route monitoring, incident triage, and targeted mitigations that mirror real production workflows.

The project is intentionally structured like a miniature production environment so I can practice diagnosing failures, writing operational automation, and documenting incidents exactly as required in a real 24/7 cloud networking role.

It includes:

- Docker Compose topology (FRRouting, VPN, load balancer, app services)
- Python and Bash tooling for detection, triage, and mitigation (experimental)
- Incident scenarios with runbooks and RCA documents
- Architecture and SOP documentation

## Stack

- FRRouting (BGP)
- Nginx (TCP/HTTP load balancer)
- WireGuard (VPN)
- Python 3 (automation, monitoring, analysis)
- Bash (operational scripts)
- Docker Compose

## Quick start

```bash
docker compose up -d
```
