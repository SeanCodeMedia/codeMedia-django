from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'


class MediaStorage(S3Boto3Storage):
    bucket_name = 'seancodemediadjango'
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False