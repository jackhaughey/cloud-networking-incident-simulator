FROM nginx:stable

# Remove default config
RUN rm /etc/nginx/conf.d/default.conf

# Copy your custom LB config
COPY nginx.conf /etc/nginx/nginx.conf

# Expose HTTP
EXPOSE 80

# Health check (optional but useful for incident drills)
HEALTHCHECK  --interval=10s --timeout=3s --retries=3 \
  CMD curl -f http://localhost/ || exit 1
