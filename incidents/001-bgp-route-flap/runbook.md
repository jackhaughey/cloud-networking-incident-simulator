# Runbook — BGP Route Flap

1. **Verify customer impact**
   - Check HTTP responses from `lb`.
   - Confirm reachability to app1/app2.

2. **Check BGP state**
   - `docker exec r2 vtysh -c "show ip bgp summary"`
   - Look for flapping peers or high `Up/Down` churn.

3. **Collect evidence**
   - Run `tools/bash/log_snapshot.sh`.
   - Save outputs under `incidents/001-bgp-route-flap/artifacts/`.

4. **Mitigation**
   - Disable unstable interface or neighbor.
   - Correct BGP configuration (AS number, timers, networks).
   - Confirm convergence and restore service.

5. **Post-incident**
   - Update `rca.md`.
   - Add SOP entry in `docs/sop-template.md`.
