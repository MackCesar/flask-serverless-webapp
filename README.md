# Flask Serverless Web Application

## Overview
This project demonstrates a serverless web application built using Flask and AWS services such as Lambda, API Gateway, DynamoDB, S3, and CloudFront. The application allows users to submit data via a web interface, which is then stored in a DynamoDB table and retrieved upon request.

## Architecture
- **AWS Lambda**: Serves as the backend logic, handling both POST and GET requests.
- **Amazon API Gateway**: Provides RESTful endpoints for the frontend to interact with the Lambda functions.
- **Amazon DynamoDB**: Stores the data submitted by users.
- **Amazon S3**: Hosts the static frontend files (HTML, CSS, JavaScript).
- **Amazon CloudFront**: Distributes the static assets globally for faster access.

## Prerequisites
- AWS account
- AWS CLI configured with your AWS credentials
- Python 3.8 or later

## Setup Instructions

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/flask-serverless-webapp.git
    cd flask-serverless-webapp
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Configure Zappa:
    Update `zappa_settings.json` with your AWS region and S3 bucket.

4. Deploy the application:
    ```sh
    zappa deploy dev
    ```

5. Set up CloudFront:
    - Create a CloudFront distribution with your S3 bucket as the origin.
    - Update frontend URLs to use the CloudFront distribution domain.

6. Sync static files to S3:
    ```sh
    aws s3 sync templates s3://YOUR_S3_BUCKET_NAME
    ```

7. Open the CloudFront distribution URL in your browser to use the app.

## Cleaning Up
```sh
zappa undeploy dev

License

MIT License
