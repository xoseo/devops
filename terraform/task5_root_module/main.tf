provider "aws" {
  region = "us-east-1"
}

module "task5_dynamodb" {
  source = "./modules/task5_dynamodb"
}

terraform {
  backend "s3" {
    bucket  = "simazu-homework-bucket"
    key     = "task5_dynamodb/terraform.tfstate"
    region  = "us-east-1"
  }
}