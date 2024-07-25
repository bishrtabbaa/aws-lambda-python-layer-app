# aws-lambda-python-layer-app

This AWS Lambda Python Layer App demonstrates how to package and deployment specific dependencies and libraries as part of your Lambda SAM deployment unit.

## 0.  Install CLI tools

* bash
* git
* aws
* sam
* python3
* pip3

## 1. Download AWS Lambda Python Layer App Repository

```
git clone https://github.com/bishrtabbaa/aws-lambda-python-layer-app
cd aws-lambda-python-layer-app
```

## 2. Build and Deploy Lambda Python Layer

```
mkdir python
cd python
pip3 install requests packaging urllib3==1.26.19 -t .
cd ..
zip -r my-aws-lambda-python-layer.zip python
aws lambda publish-layer-version --region us-east-2 --layer-name my-aws-lambda-python-layer --zip-file fileb://my-aws-lambda-python-layer.zip
aws lambda list-layers
```

## 3. Validate, Build and Deploy Lambda Python Function

```
sam validate --region us-east-2
sam deploy --guided --region us-east-2 --stack-name MyAwsLambdaPythonLayerAppStack --capabilities CAPABILITY_NAMED_IAM
```

## 4. Test Lambda Python Function

```
sam remote invoke AwsLambdaPythonLayerAppFunction --stack-name MyAwsLambdaPythonLayerAppStack 
```