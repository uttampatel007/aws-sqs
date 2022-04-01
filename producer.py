import boto3


class SQSProducerClient:
    """
    SQS Client class to produce message
    Reference : https://docs.aws.amazon.com/code-samples/latest/catalog/python-sqs-message_wrapper.py.html
    """
    def __init__(self):
        # initialize boto3 client
        self.client = boto3.client(
            'sqs', # service name
            aws_access_key_id="YOUR_ID",
            aws_secret_access_key="YOUR_KAY",
            region_name="YOUR_NAME"
        )
        self.queue_url="URL"
        
        print("SQSClient Initialize!")

    def send_message(self, message):
        response = self.client.send_message(
            MessageGroupId='586474de88e03',
            QueueUrl=self.queue_url,
            # DelaySeconds=10,
            MessageAttributes={
                'Title': {
                    'DataType': 'String',
                    'StringValue': 'The Whistler'
                },
                'Author': {
                    'DataType': 'String',
                    'StringValue': 'Nayan Sakhiya'
                },
                'WeeksOn': {
                    'DataType': 'Number',
                    'StringValue': '6'
                }
            },
            MessageBody=message
        )
        print(f"Message with id {response['MessageId']} created!")
    

sqs_obj = SQSProducerClient()
sqs_obj.send_message("Hello World!")