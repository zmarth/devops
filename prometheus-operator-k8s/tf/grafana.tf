resource "helm_release" "grafana" {
  name = "grafana"

  repository        = "https://grafana.github.io/helm-charts"
  chart             = "grafana"
  namespace         = "monitoring"
  create_namespace  = true 
  version           = "6.50.7"

  set {
    name  = "image.tag"
    value = "9.3.6"
  }

  set {
    name  = "adminPassword"
    value = "devops123"
  }

  set {
    name  = "persistance.enabled"
    value = "true"
  }

  set {
    name  = "persistance.size"
    value = "8Gi"
  }
}