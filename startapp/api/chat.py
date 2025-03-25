
from rest_framework.response import Response
from rest_framework.views import APIView
from dotenv import load_dotenv

from startapp.models import ChatData
from startapp.serializers import CountrySerializer

from openai import OpenAI
import tiktoken  
import os

## HELPER FUNCTIONS ##
def num_tokens(message: dict, model: str = 'gpt-4o-mini') -> int:
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = 3
    for key, value in message.items():
        num_tokens += len(encoding.encode(value))
    num_tokens += 3
    return num_tokens

## API VIEWS ##
class CountryChat(APIView):
    def get(self, request):
        queryset = ChatData.objects.values('country', 'isoalpha2').distinct().order_by('country')
        return Response(CountrySerializer(queryset, many=True).data)

class ChatCompletion(APIView):
    def post(self, request):
        load_dotenv()
        history = request.data.get('history', []) 
        country = request.data.get('country', {})
        
        #Filters Demo Data per Country
        queryset = ChatData.objects.filter(country = country['name']).values('country', 'phenomenon_time_reference_year', 'total_monitoring_sites', 
                                                                                  'water_body_category', 'matrix', 'proportion_of_confirmed_samples',
                                                                                  'loq_value', 'number_of_collected_samples', 'number_samples_below_loq',
                                                                                  'mean_concentration', 'minimum_recorded_value', 'maximum_recorded_value', 'unit_of_measure').order_by('-phenomenon_time_reference_year')[:668]
        
        

        formatted_string = "\n".join(
            " | ".join(f"{key}: {value}" for key, value in item.items()) 
            for item in queryset
        )
        
        systemPrompt_init = """Tu es un expert en analyse des données de qualité de l'eau. Utilise les données suivantes pour fournir une analyse détaillée et pertinente :
                        Données : {data}
                        Merci de prendre en compte ces informations pour évaluer la qualité de l'eau et fournir des conclusions précises et explique pour des utilisateurs n'ayant aucune expertise dans ce domaine.
                    """

        systemPrompt = systemPrompt_init.format(data=formatted_string)
        systemPromptDict = {'role' : 'system', 'content' : systemPrompt}
        userRequest = history[-1]
        
        max_output_tokens = 1000
        max_input_tokens = 100000
        
        history=history[:-1]
        messages=[]
        totalTokenCount = num_tokens(systemPromptDict) + num_tokens(userRequest)
        for message in reversed(history):
            potentialToken = num_tokens(message)
            if totalTokenCount + potentialToken > max_input_tokens:
                print("Reached max tokens of %d, history will be truncated", max_input_tokens)
                break
            messages.append(message)
            totalTokenCount += potentialToken
        
        messages.insert(0, systemPromptDict)
        messages.append(userRequest)
        
         
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        answer = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0,
            max_completion_tokens=max_output_tokens
        )

        return Response({'message': answer.choices[0].message.content, 'history' : messages})


