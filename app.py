from flask import Flask, render_template, request
import boto3
import uuid

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb', region_name='YOUR_AWS_REGION')
table = dynamodb.Table('YourDynamoDBTable')

@app.route('/')
def index():
    response = table.scan()
    items = response['Items']
    return render_template('index.html',items=items)

@app.route('/add',methods=['POST'])
def add():
    items = {
        'id':str(uuid.uuid4()),
        'data':request.form['data']
    }
    table.put_item(Item=item)
    return 'Item added', 200

if __name__ == '__main__':
    app.run(debug=True)