from django.conf import settings
from storages.backends.s3boto import S3BotoStorage


class MediaStorage(S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION


class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION
