resource "aws_cloudwatch_event_rule" "start_instances_event_rule" {
  name = "start_instances_event_rule"
  description = "Starts stopped EC2 instances"
  schedule_expression = var.schedule_start
  depends_on = [aws_lambda_function.ec2_start_scheduler_lambda]
}

resource "aws_cloudwatch_event_rule" "stop_instances_event_rule" {
  name = "stop_instances_event_rule"
  description = "Stops running EC2 instances"
  schedule_expression = var.schedule_stop
  depends_on = [aws_lambda_function.ec2_stop_scheduler_lambda]
}

resource "aws_cloudwatch_event_target" "start_instances_event_target" {
  target_id = "start_instances_lambda_target"
  rule = aws_cloudwatch_event_rule.start_instances_event_rule.name
  arn = aws_lambda_function.ec2_start_scheduler_lambda.arn
}

resource "aws_cloudwatch_event_target" "stop_instances_event_target" {
  target_id = "stop_instances_lambda_target"
  rule = aws_cloudwatch_event_rule.stop_instances_event_rule.name
  arn = aws_lambda_function.ec2_stop_scheduler_lambda.arn
}

resource "aws_lambda_permission" "allow_cloudwatch_to_call_start_scheduler" {
  statement_id = "AllowExecutionFromCloudWatch"
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.ec2_start_scheduler_lambda.function_name
  principal = "events.amazonaws.com"
  source_arn = aws_cloudwatch_event_rule.start_instances_event_rule.arn
}

resource "aws_lambda_permission" "allow_cloudwatch_to_call_stop_scheduler" {
  statement_id = "AllowExecutionFromCloudWatch"
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.ec2_stop_scheduler_lambda.function_name
  principal = "events.amazonaws.com"
  source_arn = aws_cloudwatch_event_rule.stop_instances_event_rule.arn
}

resource "aws_iam_role" "ec2_start_stop_scheduler" {
  name = "ec2_start_stop_scheduler"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

data "aws_iam_policy_document" "ec2_start_stop_scheduler" {
  statement {
      actions = [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ]
      resources = [
        "arn:aws:logs:*:*:*",
      ]
    }

    statement {
      actions = [
        "ec2:Describe*",
        "ec2:Stop*",
        "ec2:Start*"
      ]
      resources = [
          "*",
      ]
    }

}

resource "aws_iam_policy" "ec2_start_stop_scheduler" {
  name = "ec2_access_scheduler"
  path = "/"
  policy = data.aws_iam_policy_document.ec2_start_stop_scheduler.json
}

resource "aws_iam_role_policy_attachment" "ec2_access_scheduler" {
  role       = aws_iam_role.ec2_start_stop_scheduler.name
  policy_arn = aws_iam_policy.ec2_start_stop_scheduler.arn
}

data "archive_file" "start_scheduler" {
  type        = "zip"
  source_file = "start_instances.py"
  output_path = "start_instances.zip"
}

data "archive_file" "stop_scheduler" {
  type        = "zip"
  source_file = "stop_instances.py"
  output_path = "stop_instances.zip"
}

resource "aws_lambda_function" "ec2_start_scheduler_lambda" {
  filename = data.archive_file.start_scheduler.output_path
  function_name = "start_instances"
  role = aws_iam_role.ec2_start_stop_scheduler.arn
  handler = "start_instances.start_instances"
  runtime = var.runtime
  timeout = var.timeout
  memory_size = var.memorysize
  source_code_hash = data.archive_file.start_scheduler.output_base64sha256
}

resource "aws_lambda_function" "ec2_stop_scheduler_lambda" {
  filename = data.archive_file.stop_scheduler.output_path
  function_name = "stop_instances"
  role = aws_iam_role.ec2_start_stop_scheduler.arn
  handler = "stop_instances.stop_instances"
  runtime = var.runtime
  timeout = var.timeout
  memory_size = var.memorysize
  source_code_hash = data.archive_file.stop_scheduler.output_base64sha256
}