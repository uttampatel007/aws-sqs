from datetime import datetime

class Car(object):
    """
    gRPC Config class to get configs from environment
    """

    def __init__(self,color):
        self.color = color

    # dunder methods / magical methods
    

class_obj = Car("red")
print(class_obj)

today = datetime(2010, 1, 1)
print(today)


"""
{'ResponseMetadata': {
                        'RequestId': '4aa5a59f-4416-5d81-a2fb-ff20e42eeccc', 
                        'HTTPStatusCode': 200, 
                        'HTTPHeaders': {
                                'x-amzn-requestid': '4aa5a59f-4416-5d81-a2fb-ff20e42eeccc', 
                                'date': 'Thu, 31 Mar 2022 12:26:52 GMT', 
                                'content-type': 'text/xml', 
                                'content-length': '240'
                            }, 
                        'RetryAttempts': 0}
                    }
"""