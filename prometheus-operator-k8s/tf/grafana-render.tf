data "helm_template" "grafana" {
  name = "grafana"

  repository        = "https://grafana.github.io/helm-charts"
  chart             = "grafana"
  namespace         = "monitoring"
  create_namespace  = true
  version           = "7.3.0"

  set {
    name    = "image.tag"
    value   = "9.3.6"
  }

  set {
    name    = "adminPassword"
    value   = "devops123"
  }

  set {
    name    = "persistance.enabled"
    value   = "true" 
  }

  set {
    name    = "persistance.size"
    value   = "8Gi" 
  }
}

resource "local_file" "grafana_manifest" {
  for_each = data.helm_template.grafana.manifests

  filename = "target/${each.key}"
  content  = each.value
}