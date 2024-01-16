from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render
from .chatbot import Chatbot
from chatbot_project.settings import DEFAULT_TASK_VALUE

class Chat(View):
    def get(self, request, *args, **kwargs):
        task = request.session.get('task') or DEFAULT_TASK_VALUE
        context = {'task': task}
        return render(request, 'chatbot_app/chat.html', context=context)


@method_decorator(csrf_exempt, name='dispatch')
class ChatWithGptAjaxView(View):
    def post(self, request, *args, **kwargs):
        user_input = request.POST.get('message')
        new_task = request.POST.get('new_task')
        if new_task:
            request.session['task'] = new_task
            return JsonResponse({'message': 'Task updated to: ' + new_task})
        
        api_key = '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'  # Replace with your API key

        chatbot = Chatbot(api_key, request.session)
        response_message = chatbot.chat(request, user_input)
        chatbot.update_session(request.session)

        return JsonResponse({'message': response_message})

