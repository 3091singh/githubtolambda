import unittest
from unittest.mock import MagicMock
from your_lambda_function_file import lambda_handler  # Replace with the actual filename

class TestLambdaHandler(unittest.TestCase):
    def test_lambda_handler(self):
        # Mock S3 event
        s3_event = {
            'Records': [
                {
                    's3': {
                        'bucket': {'name': 'satwinder'},
                        'object': {'key': 'test.csv'}
                    }
                }
            ]
        }

        # Mock S3 client and response
        s3_client = MagicMock()
        s3_client.get_object.return_value = {
            'Body': MagicMock(read=MagicMock(return_value='1,John,Doe\n2,Jane,Smith\n')),
        }

        # Replace the Boto3 S3 client with the mock
        lambda_handler.s3 = s3_client

        # Capture printed output
        with unittest.mock.patch('builtins.print') as mock_print:
            # Call the lambda_handler function
            lambda_handler.lambda_handler(s3_event, None)

            # Add your assertion here if needed
            mock_print.assert_called_with('Done processing the file!')

if __name__ == '__main__':
    unittest.main()
