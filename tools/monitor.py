import subprocess
import time

ROUTERS = ["r1", "r2", "r3"]

def show_bgp_summary(router):
    cmd = ["docker", "exec", router, "vtysh", "-c", "show ip bgp summary"]
    return subprocess.run(cmd, capture_output=True, text=True)

def main():
    while True:
        print("=== BGP ROUTE MONITOR ===")
        for r in ROUTERS:
            result = show_bgp_summary(r)
            print(f"\n[{r}]")
            print(result.stdout)
        # naive anomaly detection: look for 'Idle' or 'Active'
        # in a real version you'd parse peers and states
        time.sleep(30)

if __name__ == "__main__":
    main()
