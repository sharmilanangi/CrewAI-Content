import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath("."))

print("Python path:", sys.path)
print("Current directory:", os.getcwd())

try:
    # Import and run your Flask app
    print("Attempting to import app...")
    from src.content_creation_flow.main import app
    print("Successfully imported app")
    
    if __name__ == "__main__":
        print("Starting Flask server...")
        app.run(debug=True, host='0.0.0.0', port=5001)
except Exception as e:
    print(f"Error importing app: {e}")
    import traceback
    traceback.print_exc() 