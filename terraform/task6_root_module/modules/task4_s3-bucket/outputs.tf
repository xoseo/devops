output "bucket_name" {
  value       = aws_s3_bucket.b.id
  description = "The name of the created Bucket"
}
output "bucket_arn" {
  value       = aws_s3_bucket.b.arn
  description = "The arn of the created Bucket"
}