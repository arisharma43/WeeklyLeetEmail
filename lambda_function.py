#import requests
# bs4 import BeautifulSoup 
import json
import boto3
import os

def lambda_handler(event, context):
    dynamodb=boto3.resource('dynamodb')
    ses = boto3.client('ses')
    
    table=dynamodb.Table('dailyLeet')
    
    # trans = {}
    # trans['Count'] = '0'
    # trans['actualCount'] = 0
    
    # response1=table.put_item(Item=trans)
    
    
    response1=table.get_item(
        Key={
            'Count':'0'
        }    
    )
    item=response1['Item']
    actualCount=item['actualCount']
    actualCount=int(actualCount)

    check_list=[]
    
    #actualCount=0
	
    body = "Hi, this is an automated message from Ari, captain of CS Club. Find your daily leetcode problem below! \n Attempt the problem on your own first and if you're stuck then check the community tab for the solution. If you don't understand any part of the solution, come talk with the captains after or before the club meeting, and we can discuss it.\n"
    
    with open("question_links.txt","r") as f:
    	lines=f.readlines()
    	body=body+str(lines[actualCount])
    

    ses.send_email(
	    Source = 'arisharma2017@gmail.com',
	    Destination = {
		    'ToAddresses': [
			    'arisharma2014@hotmail.com'
		    ]
	    },
	    Message = {
		    'Subject': {
			    'Data': 'Weekly LeetCode!',
			    'Charset': 'UTF-8'
		    },
		    'Body': {
			    'Text':{
				    'Data': body,
				    'Charset': 'UTF-8'
			    }
		    }
	    }
    )
    
    actualCount+=1
    table.update_item(
    Key={
        'Count':'0'
    },
    UpdateExpression='SET actualCount = :val1',
    ExpressionAttributeValues={
        ':val1': actualCount
    }
    )
    
    response3 = table.get_item(
    Key={
            'Count':'0'
        }
    )
    item = response3['Item']
    print(item)
    
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully sent email from Lambda using Amazon SES')
    }
