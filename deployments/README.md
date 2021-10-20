## Volume

Make a mount point for the volume used by the postgres container:

```shell
sudo mkdir -p /data/srepostgres        # /data/srepostgres is used in sre-db.yaml
```

## Secret

Create passwords via the k8s secret commands:

```shell
kubectl create secret generic postgres-pass --from-literal=password=<your_postgres_password>
kubectl create secret generic django-secret-key --from-literal=secret-key=<your_secret_key>
```

## Deploy

Modify `sre-ingress.yaml`, change `- host: sre-dev.minamiktr.com` to specify your domain name

```shell
kubectl label nodes $(hostname) storage=database
```

```shell
kubectl apply -f sre-db.yaml
# Verify it's running
kubectl get pods
```

```shell
kubectl apply -f sre-app.yaml
# Verify it's running
kubectl get pods
```

```shell
kubectl apply -f sre-nginx.yaml
# Verify it's running
kubectl get pods
```

```shell
kubectl apply -f sre-ingress.yaml
# Verify it's running
kubectl get ingress
```
