import boto3
import sys

def copy_between_buckets(src, dst):
	s3 = boto3.resource('s3')
	src_bucket = src
	dst_bucket = dst
	buckets_list = [b.name for b in s3.buckets.all()]

	if not isinstance(src, list):
		print("src_bucket should be a list")
		sys.exit()

	if dst_bucket not in buckets_list:
		s3.create_bucket(Bucket=dst_bucket)
		dst_bucket = s3.Bucket(dst_bucket)
		dst_bucket.wait_until_exists()
		print(f"Created {dst_bucket.name} bucket")
		dst_bucket = dst_bucket.name

	dst_bucket = s3.Bucket(dst_bucket)
	for src_b in src_bucket:
		src_b = s3.Bucket(src_b)
		for file in src_b.objects.all():
			src_file = { 'Bucket': file.bucket_name,
			'Key': file.key, }
			dst_bucket.copy(src_file, file.key)


#copy_between_buckets(['simazu-bucket1', 'simazu-bucket2'], 'simazu-bucket3')
