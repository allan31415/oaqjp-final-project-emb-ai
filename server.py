from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_det():
    text_to_analyze = request.args.get('textToAnalyze')
    analyzed_text = emotion_detector(text_to_analyze)
    dominant_emotion = analyzed_text['dominant_emotion']
    items = list(analyzed_text.items())
    emotions = ", ".join([f"'{k}': {v}" for k, v in items[:-1]])
    last_emotion = last_item = f"'{items[-1][0]}': {items[-1][1]}"
    emotions_string = f"{emotions} and {last_emotion}"
    return print(f"For the given statement, the system response is {emotions_string}. The dominant emotion is {dominant_emotion}.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


