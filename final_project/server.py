from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector



# Create an instance of the Flask class
app = Flask("Emotion Detector")


@app.route("/emotionDetector") #This path must match with path in mywebscript.js
def sent_detector():

    #Get the text input from the user, 'textToAnalyze' is the query parameter
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract emotion scores from the response dictionary
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score =response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Check if a dominant emotion is detected
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    else:
        # Return a formatted response with the emotion scores and dominant emotion
        return "For the given statement, the system response is 'anger':{}, 'disgust':{}, 'fear':{}, 'joy':{}. The dominant emotion is {}".format(anger_score, disgust_score, fear_score, joy_score, dominant_emotion)     
     
@app.route("/")
def render_index_page():
    return render_template('index.html')


#Run the application on host: 0.0.0.0 (or localhost) on port number 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)