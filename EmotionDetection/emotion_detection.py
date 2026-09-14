import requests


def emotion_detector(text_to_analyze):
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(
        url,
        json=input_json,
        headers=headers
    )

    response_data = response.json()

    emotion_predictions = response_data["emotionPredictions"][0]
    emotions = emotion_predictions["emotion"]

    dominant_emotion = max(emotions, key=emotions.get)

    emotions["dominant_emotion"] = dominant_emotion

    return emotions
    from emotion_detection import emotion_detector
    from .emotion_detection import emotion_detector
result = emotion_detector("I am so happy I am having fun")
print(result)