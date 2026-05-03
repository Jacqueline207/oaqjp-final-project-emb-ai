"""
A Flask server for an emotion detection application using pylint 
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector


#make sure to define app as Emotion Detector
app = Flask("Emotion Detector")


#making sure that the flask decorator for the app is calling the funtoin /emotionDetector
@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    Analyzing text and returning the formatted output
    """
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    #check for input (because should fail with blank entries all emotions would have to be blank)
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!" , 400

    #get results form emotion_detection
    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant_emotion = result["dominant_emotion"]
    #now to complete the proper format and return the output

    output = (
        "For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    return output

@app.route("/")
def render_index_page():
    """
    Rendering the index
    """
    return render_template("index.html")

if __name__ == "__main__":
    #in order to view this on the browser, make sure host
    # is 0.0.0.0 for external access on this browser
    app.run(host="0.0.0.0", port=5000)
