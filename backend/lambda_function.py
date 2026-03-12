import json
import boto3



def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('visitor_count')
    response = table.update_item(Key={'id':'resume'},
    UpdateExpression='ADD #count :increment',
    ExpressionAttributeNames={ '#count': 'count' },

    ExpressionAttributeValues={ ':increment': 1 },
    ReturnValues='UPDATED_NEW'
    )
    count = int(response['Attributes']['count'])
    return{
        'statusCode':200,
        'headers':{
            'Access-Control-Allow-Origin':'*'

        },
        'body':json.dumps({
            'count':count
        })
    }

