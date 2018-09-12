import boto3
import click                        #used to interact with command line arguments

session = boto3.Session(profile_name='mfprod-bhushan.naik')
s3 = session.resource('s3')

@click.group()                      #cli decoratpr
def cli():
    "Webotron deploys websites to AWS"
    pass

@cli.command('list-buckets')      #cli decorator
def list_buckets():
    "List all S3 buckets"
    for bucket in s3.buckets.all():
        print (bucket)

@cli.command('list-bucket-objects')     #cli decorator
@click.argument('bucket_name')
def list_bucket_objects(bucket_name):
    "List bucket objects"
    for obj in s3.Bucket(bucket_name).objects.all():
        print(obj.key)

if __name__ == '__main__':      #Staring point. Will run if run as a script, if imported as module, it won't run.
    print("Hello, World!")
    cli()
