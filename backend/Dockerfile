FROM python:3.10.20-alpine

WORKDIR /var/test-assignment
COPY /var/test-assignment/backend/app.py .

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
RUN chown -R appuser:appgroup /var/test-assignment
USER appuser

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD wget -qO- http://localhost:8080/ || exit 1

CMD ["python", "-u", "app.py"]