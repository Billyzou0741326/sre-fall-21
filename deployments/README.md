## Secret

```shell
kubectl create secret generic postgres-pass --from-literal=password=<your_postgres_password>
kubectl create secret generic django-secret-key --from-literal=secret-key=<your_secret_key>
```

```shell
kubectl apply -f sre-db.yaml
```

```shell
kubectl apply -f sre-app.yaml
```
