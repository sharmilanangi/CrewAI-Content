#!/usr/bin/env python
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from src.content_creation_flow.flow import ContentCreationFlow, ContentCreationState

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/content', methods=['POST'])
def social_media_content():
    """
    Endpoint to run the Content Creation Crew.
    """
    data = request.json
    print(data)
    social_media_platform = data.get('social_media_platform', "twitter")
    user_persona = data.get('user_persona', "organizer")
    event_name = data.get('event_name', "")
    user_opinion = data.get('user_opinion', "")
    highlighted_points = data.get('highlighted_points', [])
    transcript = data.get('transcript', "")
    
    if transcript == "":
        return jsonify({"social_media_content": "Nothing happened at the event. Please wait!!" }), 400
    # Create a new crew instance each time to avoid tool assignment issues
    flow = ContentCreationFlow()
    result = flow.kickoff(
        inputs={
            "social_media_platform": social_media_platform,
            "user_persona": user_persona,
            "event_name": event_name,
            "user_opinion": user_opinion,
            "highlighted_points": highlighted_points,
            "transcript": transcript
        }
    )

    return jsonify({"social_media_content": result})

if __name__ == "__main__":
    app.run(debug=True)