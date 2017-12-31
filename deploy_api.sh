#!/bin/bash

BUCKET=new-year-eve-options-bucket
REGION=ap-south-1
ACCOUNT_ID=613530786381
STACK_NAME=NewYearEveOptions

aws s3 mb s3://$BUCKET --region $REGION
cat > ./s3_policy.json <<EOM
{
  "Version": "2012-10-17",
  "Id": "123",
  "Statement" : [
    {
      "Sid" : "",
      "Effect": "Allow",
      "Prinicipal": "*",
      "Action": "s3:*",
      "Resource": "arn:aws:s3:::$BUCKET/*"
    }
  ]

}
EOM

aws s3api put-bucket-policy --bucket $BUCKET --policy file://s3_policy.json

sam package --template-file template.yaml --s3-bucket $BUCKET -output-template-file packaged.yaml --region $REGION

sam deploy --template-file .packaged.yaml --stack-name $STACK_NAME --capabilities CAPABILITY_IAM --reion $REGION
