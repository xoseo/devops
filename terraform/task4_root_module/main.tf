provider "aws" {
  region = "us-east-1"
}

module "task4_s3-bucket" {
  source = "./modules/task4_s3-bucket"
}

terraform {
  backend "s3" {
    bucket  = "simazu-homework-bucket"
    key     = "task4_s3-bucket/terraform.tfstate"
    region  = "us-east-1"
  }
}