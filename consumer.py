import boto3
from botocore.exceptions import ClientError

class SQSConsumerClient:
    """SQS Client class to consume and delete message"""
    def __init__(self):
        # initialize boto3 client
        self.client = boto3.client(
            'sqs', # service name
            aws_access_key_id="YOUR_ID",
            aws_secret_access_key="YOUR_KEY",
            region_name="YOUR_ZONE"
        )
        self.queue_url='URL'
        
        print("SQSClient Initialize!")

    def receive_message(self):
        response = self.client.receive_message(
            QueueUrl=self.queue_url,

            ## other optional parameters
            # AttributeNames=[
            #     'SentTimestamp'
            # ],
            MaxNumberOfMessages=1,
            # MessageAttributeNames=[
            #     'All'
            # ],
            # VisibilityTimeout=0,
            # WaitTimeSeconds=0
        )
        if response.get("Messages"):
            print(f'Message received with ID {response.get("Messages")[0].get("MessageId")}')
            # print(response)
            print(response.get("Messages")[0])
            return response.get("Messages")[0].get("ReceiptHandle")
        
        print("No message found in queue!")
        return None

    def delete_message(self,receipt_handle):
        try:
            self.client.delete_message(
                QueueUrl=self.queue_url,
                ReceiptHandle=receipt_handle
            )
            print("Message deleted successfully!")

        except ClientError as e:
            print("Error while deleting message!")
            raise e

    
sqs_obj = SQSConsumerClient()
receipt_handle = sqs_obj.receive_message()

# receipt_handle = "AQEBLRWUd8s7TCwBdJjdrzteJk1gBAptg85xg8tudAdbWpZ53NFRrn32A966fwFiCbVUnB7ZKVQ2U8WoxXoBCoDI24KSp8abOcD0Q4wZyIHuPa0b1ucJ9YuqViXDJGq+/sxLvA3lW/+tvTbv2TdFNKYMI99h1lMhwZYvyDQbexslEkTzJ+YqSi1hjIF+14wtFAzd/DBB3P6rMqooNxb0tP2b9tT0BVS2yFNJl1BlEArLsj1ybIjdoC1H1424FIKoA8iKH8ptjVWIUoPa+91sxZPpbktmJlW2/xYzz2jVF/ucN7KgPaSSuvNrYXm0t1d7emiA"
# if receipt_handle:
    # sqs_obj.delete_message(receipt_handle)