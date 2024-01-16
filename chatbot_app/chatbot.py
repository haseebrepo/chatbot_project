import openai
from chatbot_project.settings import DEFAULT_TASK_VALUE

class Chatbot:
    def __init__(self, api_key, session_data):
        self.api_key = api_key
        self.conversation_history = session_data.get('conversation_history', "")

    def chat(self, request, user_input):
        openai.api_key = self.api_key
        prompt = f"{self.conversation_history}\nUser: {user_input}\nAI:"
        
        try:
            task = "Task: " + request.session.get('task') or DEFAULT_TASK_VALUE
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", 
                     "content": task},
                    {"role": "user", "content": prompt}
                ]
            )
            response_message = response.choices[0].message['content']
            self.conversation_history += f"\nUser: {user_input}\nChatbot: {response_message}"
            return response_message
        except Exception as e:
            return f"An error occurred: {e}"

    def update_session(self, session_data):
        session_data['conversation_history'] = self.conversation_history
