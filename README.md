# SRE Site

## Test

## Deploy

There are multiple steps to deploying the site with docker:

Initialize docker containers

```shell
docker-compose up --no-start    # create containers, volumes, network, etc
```

Set up postgres server

```shell
docker-compose start postgres   # starts the postgresql container
```

Brings up all services

```shell
docker-compose up -d            # starts all services (backend)
```

After the services are started up and running, proceed to set up some one-time configuration for django 

### One-time conifguration

```shell
docker-compose exec backend python manage.py makemigrations     # init database migrations
docker-compose exec backend python manage.py migrate            # run migrations
docker-compose exec backend python manage.py createsuperuser    # create admin accounts for the web app
docker-compose exec backend python manage.py collectstatic      # collect static files
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
