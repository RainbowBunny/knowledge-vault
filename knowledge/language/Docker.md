---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-11-28T16:07
---
`Dockerfile` builds the image:
- Base image
- Dependencies
- Build step
- Runtime setup
- CMD / ENTRYPOINT

`docker-compose.yml` orchestrates one or many containers:
- How to run the app’s container(s)
- Environment variables
- Volumes
- Ports
- Networks
- Dependencies between services (DB, cache, backend, frontend, etc.)

Build image:

```bash
docker build -t myapp .
```

Run a single container without compose

```bash
docker run -p LOCAL_PORT:CONTAINER_PORT myapp
```

Use `docker-compose` when:
- The project involves multiple services (DB, API, frontend, redis, rabbit…)
- Environment variables are needed
- You want automatic networking
- You want easier scaling

And run:

```bash
docker compose up
```

