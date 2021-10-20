## Volume

Make a mount point for the volume used by the postgres container:

```shell
sudo mkdir /data/srepostgres        # /data/srepostgres is used in sre-db.yaml
```

## Secret

Create passwords via the k8s secret commands:

```shell
kubectl create secret generic postgres-pass --from-literal=password=<your_postgres_password>
kubectl create secret generic django-secret-key --from-literal=secret-key=<your_secret_key>
```

## Deploy

```shell
kubectl apply -f sre-db.yaml
```

```shell
kubectl apply -f sre-app.yaml
```

```shell
kubectl apply -f sre-ingress.yaml
```
