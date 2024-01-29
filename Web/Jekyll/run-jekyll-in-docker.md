## Run Jekyll in Docker

>https://stackoverflow.com/questions/51404768/jekyll-site-running-inside-docker-container-but-localhost4000-is-not-working-on

Basically, add `--host "0.0.0.0"` in `bundle exec jekyll service` command:


`bundle exec jekyll service --host "0.0.0.0"`