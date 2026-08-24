# Incident 001 — BGP Route Flap Causing Service Outage

## Context

- r2 advertises 10.0.0.0/24 towards r1 and r3.
- A misconfiguration and interface flaps cause intermittent loss of reachability
  to the app services behind r3.

## Symptoms

- Intermittent HTTP 502/504 from `lb`.
- Increased latency and packet loss to app1/app2.
- BGP peers on r2 oscillate between `Established` and `Idle`.
