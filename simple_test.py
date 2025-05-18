import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath("."))

# Try to import the Flask app
try:
    from src.content_creation_flow.main import app
    print("Successfully imported Flask app")
    
    # Print routes
    print("\nAvailable routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint}: {rule.methods} - {rule}")
        
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc() 