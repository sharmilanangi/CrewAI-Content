import requests
import json

# Test the API
def test_get_endpoint():
    response = requests.get('http://127.0.0.1:5000/test')
    print("GET /test response:", response.status_code)
    print(response.json())

def test_post_endpoint():
    # Sample data
    data = {
        "social_media_platform": "twitter",
        "user_persona": "organizer",
        "event_name": "Test Event",
        "user_opinion": "It was great",
        "highlighted_points": ["Point 1", "Point 2"],
        "transcript": "This is a test transcript"
    }
    
    # Send POST request
    response = requests.post(
        'http://127.0.0.1:5000/content',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(data)
    )
    
    print("POST /content response:", response.status_code)
    print(response.json())

if __name__ == "__main__":
    print("Testing GET endpoint...")
    test_get_endpoint()
    
    print("\nTesting POST endpoint...")
    test_post_endpoint() 