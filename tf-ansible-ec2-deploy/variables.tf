variable "region" {
  type = string
  description = "The AWS region to deploy the infrastructure to."
}
variable "access_key" {
  type = string
  sensitive = true
  description = "The AWS access key."
}
variable "secret_key" {
  type = string
  sensitive = true
  description = "The AWS secret key."
}