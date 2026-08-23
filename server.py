''' This is the server script which handles the web responses
and decoration.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_det():
    ''' This function analyzes the response and formats it properly.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    analyzed_text = emotion_detector(text_to_analyze)
    dominant_emotion = analyzed_text['dominant_emotion']
    if dominant_emotion == "None":
        return "Invalid text! Please try again!"

    items = list(analyzed_text.items())
    emotions = ", ".join([f"'{k}': {v}" for k, v in items[:-2]])
    last_emotion = f"'{items[-2][0]}': {items[-2][1]}"
    emotions_string = f"{emotions} and {last_emotion}"
    return f"For the given statement, the system response is {emotions_string}. \
        The dominant emotion is {dominant_emotion}."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
