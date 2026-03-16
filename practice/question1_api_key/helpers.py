from openai import OpenAI, DefaultHttpxClient

# TODO: Set your API Key here
API_KEY = 'your api key here'


def text_chat(messages):
    # Everything below is fine, no need to change
    client = OpenAI(base_url='https://chatdmdi.com.cuhk.edu.hk/v1', api_key=API_KEY,
                    http_client=DefaultHttpxClient(verify=False))
    response = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    reply = response.choices[0].message.content
    result = messages + [{'role': 'assistant', 'content': reply}]
    return result


if __name__ == "__main__":
    result_messages = text_chat([{'role': 'user', 'content': 'hello'}])
    '''
    Expected Result
    [{'role': 'user', 'content': 'hello'}, {'role': 'assistant', 'content': 'Hello! How can I assist you today?'}]
    '''
    print(result_messages)