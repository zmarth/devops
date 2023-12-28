# IaC Internship tasks

## Exercise 1
* Prepare an terraform state which contains definition of existing DNS zone yourwebsite.com and import existing zone in created state.
* Import all existing DNS records in terraform code an update state with existing data.
* DO NOT delete existing zone.
Terraform
Route53

## Exercise 2
* Create with terraform 2 distinct VPC.
* Configure VPC peering between created VPCs.
* Launch 1 EC2 instance and one RDS in different VPCs.
* Configure an script to make periodically backups of re mote VPC database from EC2 instance and store in a $3 bucket.
Terraform
Ansible

## Exercise 3
* Create an Lambda function to automatically stop all VM instance with AutoStop tag in all regions everyDay at 7pm.
* Create another Lambda function to start at 8am VM instances with AutoStart tag in all regions.
EC2
Lambda
Terraform

## Exercise 4
* Install in AWS a wordpress solution with Nginx as WebServer and Private RDS database
* Expose website externally via LoadBalancer
* Register your website in DNS zone from Ex1
* and SSL certificate to your site and redirect all traffic from HTTP to HTTPS
* Configure daily backups of database
EC2
RDS
LoadBalancer
Certificate manager
Terraform
Ansible

## Exercise 5

* Prepare a solution to launch an EC2 instance (terraform)
* which automatically install Jenkins, nginx, configure nginx as loadBalancer for Jenkins
* Ceate an jenkins user "cfadmin" with predefined password.
* Store jenkins username and password in an encrypted file
EC2
AMI
Terraform
Ansible

## Exercise 6
* Install an OpenVPN server on your bastion server
* register it in DNS zone from Ex1
* Configure VPN profiles for all your team members.
* Extract Users VPN profiles on your PC
EC2
Security Groups
Terraform
Ansible

## Exercise 7
* Detect public IP of a instance created by your colleague in another VPC and region
* Create an Security group which allow access to ports from IP in previous step. (ports must be defined as variable )
* 3306
* 5432
* 1145
* 2972
* 53
* 22
* Find 2 different solutions to extract remote instance IP
Terraform

## Exercise 8
* create private ECR repositories from list
* is-backend
* is-frontend
* Is-mysql
* -is-postgres
* Add an AWS service account with permissions to upload and download ECR images
Terraform
AWS-IAM