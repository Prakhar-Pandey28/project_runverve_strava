from app import create_app

# Create the Flask app
app = create_app()

# Debug information
print("Application created successfully!")
print(f"Debug mode: {app.config['DEBUG']}")

if __name__ == '__main__':
    # Run the app with debugging enabled
    app.run(debug=True, host='0.0.0.0', port=5000)