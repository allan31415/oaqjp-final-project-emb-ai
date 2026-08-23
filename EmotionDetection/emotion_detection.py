import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = myobj, headers=headers)
    status_code = response.status_code
    if status_code == 200:
        formatted_response = json.loads(response.text)
        #extract emotion scores
        angersc = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgustsc = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fearsc = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joysc = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadnesssc = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    elif status_code == 400:
        angersc = "None"
        disgustsc = "None"
        fearsc = "None"
        joysc = "None"
        sadnesssc = "None"

    else:
        return "Something went wrong, please try again"

    #determine dominant emotion
    emotion_dict = {'anger': angersc, 
                    'disgust': disgustsc, 
                    'fear': fearsc,
                    'joy': joysc,
                    'sadness': sadnesssc}
    if status_code == 400:
        dominant_emotion = "None"
    else:
        dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    emotion_dict['dominant_emotion'] = dominant_emotion
    return emotion_dict


