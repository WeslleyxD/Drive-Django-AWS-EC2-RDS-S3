from decouple import config

#aws
AWS_SERVER_PUBLIC_KEY = config('AWS_SERVER_PUBLIC_KEY')
AWS_SERVER_SECRET_KEY = config('AWS_SERVER_SECRET_KEY')


BUCKET = config('BUCKET')