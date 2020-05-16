provider "aws" {
  region = "us-east-1"
}

module "task3_lambdas" {
  source = "./modules/task3_lambdas"
}

terraform {
  backend "s3" {
    bucket  = "simazu-homework-bucket"
    key     = "task3_lambdas/terraform.tfstate"
    region  = "us-east-1"
  }
}