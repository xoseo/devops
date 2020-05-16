provider "aws" {
  region = "us-east-1"
}

module "task6_s3-event" {
  source = "./modules/task6_s3-event"
}

terraform {
  backend "s3" {
    bucket  = "simazu-homework-bucket"
    key     = "task6-s3-event/terraform.tfstate"
    region  = "us-east-1"
  }
}
