provider "aws" {
  region = "us-east-1"
}

module "task6_s3-event" {
  source = "./modules/task6_s3-event"
  bucket_name = module.task4_s3-bucket.bucket_name
  bucket_arn = module.task4_s3-bucket.bucket_arn
}

module "task4_s3-bucket" {
  source = "./modules/task4_s3-bucket"
}

terraform {
  backend "s3" {
    bucket  = "simazu-homework-bucket"
    key     = "task6-s3-event/terraform.tfstate"
    region  = "us-east-1"
    dynamodb_table = "terraform-state-lock-dynamo"
  }
}
