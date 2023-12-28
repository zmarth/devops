resource "aws_instance" "web-master" {
  ami = "ami-0eb260c4d5475b901"
  instance_type = "t2.micro"
  key_name = "AlexKeyHome"
  vpc_security_group_ids = [aws_security_group.web-sg.id]

  tags = {
    Name = "jenkins-master"
  }
}

resource "aws_instance" "web-slave" {
  ami = "ami-0eb260c4d5475b901"
  instance_type = "t2.micro"
  key_name = "AlexKeyHome"
  vpc_security_group_ids = [aws_security_group.web-sg.id]

  tags = {
    Name = "jenkins-slave"
  }
}

resource "aws_security_group" "web-sg" {
  name = "jenkins-server-sg"

dynamic "ingress" {
  for_each = [80, 443, 22, 8080]
  content  {
    from_port  = ingress.value
    to_port    = ingress.value
    protocol   = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
egress {
  from_port        = 0
  to_port          = 0
  protocol         = "-1"
  cidr_blocks      = ["0.0.0.0/0"]
}

}
output "web-master-ip" {
  value = aws_instance.web-master.public_ip
}

output "web-slave-ip" {
  value = aws_instance.web-slave.public_ip
}