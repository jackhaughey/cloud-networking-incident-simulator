FROM alpine:latest

# Install WireGuard + required tools
RUN apk update && \
    apk add --no-cache wireguard-tools iproute2 bash

# Copy WireGuard config
COPY wg0.conf /etc/wireguard/wg0.conf

# Bring up the tunnel on container start
CMD ["wg-quick", "up", "wg0"]
