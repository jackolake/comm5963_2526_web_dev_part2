import base64
from flask import Flask, render_template, request, redirect, url_for, session
import markdown
from ..question1_api_key.helpers import text_chat

app = Flask(__name__)
app.secret_key = 'CUHK'  # Seed for generating Session ID (Do not expose!)
app.config['PERMANENT_SESSION_LIFETIME'] = 1800 # Expiry: 30 minutes
app.config['SESSION_TYPE'] = 'cachelib'  # Session as files


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
        user_input_dict = {'role': 'user', 'content': user_input}
        input_messages = [
            # This is the system message
            {'role': 'system', 'content': system_message},
            # This is the user input
            user_input_dict
        ]
        # Check if session contains history
        session_history = session.get('history', [])
        if session_history:
            input_messages = session_history + [input_messages[-1]]
        # Send to OpenAI API
        result_messages = text_chat(input_messages)
        # Save message to history for next chat
        session['history'] = result_messages
        # Before rendering, convert each content into markdown
        display_messages = []
        for message in result_messages:
            message['content'] = markdown.markdown(message['content'])
            display_messages.append(message)
        # Render in the template
        return render_template('index.html', messages=display_messages)
    return redirect(url_for('index'))

@app.route("/clear_history", methods=['GET', 'POST'])
def clear_history():
    session['history'] = []
    return redirect(url_for('index'))


@app.route("/vision", methods=['GET', 'POST'])
def vision():
    question = request.form.get("question", "What is in this image?")
    img_file = request.files.get("image")

    if not img_file or not img_file.filename:
        return render_template("vision.html", error="No image uploaded")

    # Encode image to base64 (bytes type)
    image_data = img_file.read()
    # Convert that as "string" so we can send it over to our OpenAI API
    base64_image = base64.b64encode(image_data).decode('utf-8')

    # Determine mime type
    mime_type = img_file.content_type or "image/jpeg"
    image_messages = [
        {
            "role": "system",
            "content": "You are an animal expert at a natural park in Hong Kong. Identify the animal in the image and provide educational facts."
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": question},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:{mime_type};base64,{base64_image}"
                    },
                },
            ],
        }]
    result_messages = text_chat(messages=image_messages)
    reply = result_messages[-1]['content']
    reply_html = markdown.markdown(reply)
    return render_template("vision.html", reply=reply_html, question=question,
                           image_data=base64_image)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
