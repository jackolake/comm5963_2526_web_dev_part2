from flask import Flask, render_template, request, redirect, url_for
from ..question1_api_key.helpers import text_chat

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form.get("message")

    if user_input:
        system_message = (
            "You are a friendly and professional chatbot for a natural park in Hong Kong. "
            "Your goal is to educate the public about animals, especially Red Pandas. "
            "Keep your tone informative, engaging, welcoming but very concise."
        )
        # Prepare the messages to be sent
        input_messages = [
            # This is the system message
            {'role': 'system', 'content': system_message},
            # This is the user input
            {'role': 'user', 'content': user_input}
        ]
        # Send to OpenAI API
        result_messages = text_chat(input_messages)
        # Render in the template
        return render_template('index.html', messages=result_messages)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
