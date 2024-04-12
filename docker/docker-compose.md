## Docker compose

It's been awhile since last time I was working on the docker. I forget about how dockerfile was build and how to use docker compose. This project help me pick up what I forget.

1. Create `docker-compose.yml`

```docker
version: "3"

services:
  web:
    build: .
    command: bundle exec jekyll serve --trace --livereload --host "0.0.0.0"
    ports:
      - "4000:4000"
```  

2. Run followings in bash

```bash
docker-compose up
```
