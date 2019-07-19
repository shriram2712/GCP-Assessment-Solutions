# Basic operations on objects using the python client libraries

#import the storage module
from google.cloud import storage

import logging

#Initialize the logger
logging.basicConfig(filename="q8.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 
#Creating an object 
logger=logging.getLogger() 
#set logger to debug
logger.setLevel(logging.DEBUG) 

#object upload method
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)
    logger.info("Object uploaded")	
    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

#object download method
def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)
    logger.info("Object downloaded")	
    print('Blob {} downloaded to {}.'.format(
        source_blob_name,
        destination_file_name))

#Copy object method
def copy_blob(bucket_name, blob_name, new_bucket_name, new_blob_name):
    """Copies a blob from one bucket to another with a new name."""
    storage_client = storage.Client()
    source_bucket = storage_client.get_bucket(bucket_name)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.get_bucket(new_bucket_name)

    new_blob = source_bucket.copy_blob(
        source_blob, destination_bucket, new_blob_name)
    logger.info("Object copied")	
    print('Blob {} in bucket {} copied to blob {} in bucket {}.'.format(
        source_blob.name, source_bucket.name, new_blob.name,
        destination_bucket.name))

#Move object method
def move_blob(bucket_name, blob_name, new_bucket_name, new_blob_name):
    """Copies a blob from one bucket to another with a new name."""
    storage_client = storage.Client()
    source_bucket = storage_client.get_bucket(bucket_name)
    source_blob = source_bucket.blob(blob_name)
    destination_bucket = storage_client.get_bucket(new_bucket_name)

    new_blob = source_bucket.copy_blob(
        source_blob, destination_bucket, new_blob_name)
    source_blob.delete()	
    logger.info("Object moved")		
    print('Blob {} in bucket {} moved to blob {} in bucket {}.'.format(
        source_blob.name, source_bucket.name, new_blob.name,
        destination_bucket.name))

# DElete object method
def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.delete()
    logger.info("Object deleted")	
    print('Blob {} deleted.'.format(blob_name))

upload_blob("shriram-a1-q5", "/home/shriram/Pictures/1.png", "1.png")
download_blob("a1q5bucket", "Sample1.txt", "/home/shriram/Downloads/sample.txt")
copy_blob("shriram-a1-q5-2", "1.png", "shriram-a1-q5", "1.png")
move_blob("shriram-a1-q5-2", "1.png", "shriram-a1-q5", "1.png")
delete_blob("shriram-a1-q5", "1.png")

