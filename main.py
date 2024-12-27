from flask import Flask, request

app = Flask(__name__)


@app.route('/send-message', methods=['POST'])
def send_message():
    print("Data received from Webhook is (Send Message): ", request.json)
    return "Webhook received!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
