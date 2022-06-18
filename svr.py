from flask import Flask, request, abort, Response

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'Success!', 200
    else:
         abort(400)

def listen():
    data = json.loads(request.data)
    print(data)

def respond():
    print(request.json) #Handle webhook request
    return Response(status=200)



if __name__ == '__main__':
    app.run()