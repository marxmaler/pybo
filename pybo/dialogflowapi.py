import os
import dialogflow
from google.api_core.exceptions import InvalidArgument
from google.protobuf.json_format import MessageToJson
import json

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'shopping-vrwt-7062c2e8bdc3.json' #환경 설정 #키 파일, 만약 dialogflowapi와 같은 경로에 없다면 경로를 구체적으로 명시해줘야 함.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'C:\Users\marxm\Desktop\pythonProject\FlaskProject\pybo\shopping-vrwt-7062c2e8bdc3.json' #환경 설정 #키 파일, 만약 dialogflowapi와 같은 경로에 없다면 경로를 구체적으로 명시해줘야 함.

DIALOGFLOW_PROJECT_ID = 'shopping-vrwt'
DIALOGFLOW_LANGUAGE_CODE = 'ko'

session_client = dialogflow.SessionsClient()

def chat(text, session_id = 'me'):
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise

    # print(response.query_result.fulfillment_text) #response만 출력하면 유니코드로 이상한 게 나오는데, 이런 식으로 키 값 넣고 찾아가서 출력하면 멀쩡하게 나옴.
    result = json.loads(MessageToJson(response))
    # print(response.query_result.fulfillment_text)
    return response.query_result.fulfillment_text

chat('안녕', '12345')