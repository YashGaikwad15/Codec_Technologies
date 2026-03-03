from flask import Flask, render_template, request, jsonify
from chatbot.model import get_intent
from chatbot.intents import INTENTS, RESPONSES
from chatbot.database import init_db, save_chat

app = Flask(__name__)
init_db()  # initialize DB

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    # Detect intent
    labels = list(INTENTS.keys())
    intent = get_intent(user_message, labels)

    # Get response
    response = RESPONSES.get(intent, "I'm not sure I understand.")
    
    # Save chat to database
    save_chat(user_message, response)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
