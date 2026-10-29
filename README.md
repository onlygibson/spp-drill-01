# spp-drill-01: files-api

> **Warning:** this service is **intentionally vulnerable**. It is a practice repo for security platform work. Do not deploy it anywhere public or reuse its code.

A small internal API handed over by a developer team. Your job, as the security platform engineer, is to find its problems, decide what matters, fix them, and prove the fixes work. The work is assigned as tickets DRILL-1 to DRILL-6.

## Endpoints

| Method | Path | What it does |
| --- | --- | --- |
| GET | `/health` | Liveness check |
| GET | `/files?name=report.txt` | Shows details for one stored file |
| POST | `/image-size` | Returns width and height of an uploaded image (form field `file`) |

## Run locally

```bash
docker build -t files-api:0.1.0 .
docker run -d --name files-api -p 8080:8080 files-api:0.1.0
curl localhost:8080/health
curl "localhost:8080/files?name=report.txt"
```

## Results

| Metric | Before | After |
| --- | --- | --- |
| Dependabot alerts | TBD | TBD |
| Code scanning alerts | TBD | TBD |
