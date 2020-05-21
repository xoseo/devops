resource "aws_dynamodb_table" "basic-dynamodb-table" {
  name           = "task5_dynamodb_table"
  billing_mode   = "PAY_PER_REQUEST"
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
