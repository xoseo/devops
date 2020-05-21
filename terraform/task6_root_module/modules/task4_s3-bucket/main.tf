resource "aws_s3_bucket" "b" {
  bucket = "simazu-task4-bucket"
  acl    = "private"

  tags = {
    Name        = "Homework 2 task4 bucket"
    Environment = "Homework 2"
  }
}
