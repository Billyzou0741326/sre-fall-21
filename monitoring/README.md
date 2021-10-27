# Monitoring

Before applying the manifests, create the k8s secret first:

```shell
kubectl create secret generic -n kube-system monitor-secret --from-env-file=monitoring/.env
```

Spin up kube-state-metrics:

```shell
kubectl apply -f https://raw.githubusercontent.com/kubernetes/kube-state-metrics/release-2.2/examples/standard/service-account.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes/kube-state-metrics/release-2.2/examples/standard/cluster-role.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes/kube-state-metrics/release-2.2/examples/standard/cluster-role-binding.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes/kube-state-metrics/release-2.2/examples/standard/deployment.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes/kube-state-metrics/release-2.2/examples/standard/service.yaml
```
