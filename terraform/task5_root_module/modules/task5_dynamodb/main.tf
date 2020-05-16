resource "aws_dynamodb_table" "basic-dynamodb-table" {
  name           = "task5_dynamodb_table"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "file_name"

  attribute {
    name = "file_name"
    type = "S"
  }

  tags = {
    Name        = "Homework 2 task 5 dynamodb"
    Environment = "Homework 2"
  }
}
