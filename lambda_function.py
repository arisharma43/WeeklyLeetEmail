#import requests
# bs4 import BeautifulSoup 
import json
import boto3

def lambda_handler(event, context):
    
    ses = boto3.client('ses')
    
    check_list=[]
    
    # with open("question_links.txt","r") as f:
    # 	#lines=f.readlines()
    # 	line=f.readline()
    # 	while line:
    # 		check=line.strip()
    # 		if check[0:30]=='https://leetcode.com/problems/':
    # 			check_list.append(check)
    # 		line=f.readline()
    		
    # 		print(check_list)
	
    count=0
    body = "Hi, this is an automated message from Ari. Find your daily leetcode problem below! Attempt the problem on your own first and if you're stuck then check the community tab for the solution. If you don't understand any part of the solution, come talk with us after or before the club meeting, and we can discuss it.\n"
    
    with open("question_links.txt","r") as f:
    	lines=f.readlines()
    	body=body+str(lines[count])
    

    ses.send_email(
	    Source = 'sender@gmail.com',
	    Destination = {
		    'ToAddresses': [
			    'reciever@gmail.com'
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
    count+=1
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully sent email from Lambda using Amazon SES')
    }
