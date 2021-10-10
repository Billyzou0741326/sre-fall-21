# SRE Site

## Test

## Deploy

First, ensure `.env` file is present under the top level of the project with the correct configuration.

There are multiple steps to deploying the site with docker:

Initialize docker containers

```shell
docker-compose up --no-start    # create containers, volumes, network, etc
```

Set up postgres server

```shell
docker-compose start postgres   # starts the postgresql container
```

Bring up all services

```shell
docker-compose up -d --build    # starts all services (backend)
docker cp sre-fall-21-site_backend_1:/app/static ./ && docker cp ./static/ sre-fall-21-site_frontend_1:/app/    # copy static files to nginx
```

After the services are started up and running, proceed to set up some one-time configuration for django 

### One-time conifguration

```shell
docker-compose exec backend python manage.py createsuperuser    # create admin accounts for the web app
```

## Develop

This workflow aims to resolve commit history conflicts.

After committing (`git commit`) new changes, before pushing to the remote repository:

```shell
git remote update               # checks for new commits from the remote repository
git rebase remotes/origin/main  # rebase, or align commit history, with the remote main branch
```

If rebase fails due to merge conflict, resolve the conflict and commit the resolution.

Then push to your branch and the main branch:

```shell
git push origin <your_branch>
git push origin HEAD:main       # main branch
```
