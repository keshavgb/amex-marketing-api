from src.app import create_app

app = create_app()

if __name__ == "__main__":
    print("Starting Marketing Content API...")
    print("")
    print("Try these URLs in your browser:")
    print("  http://127.0.0.1:5000/api/campaigns")
    print("  http://127.0.0.1:5000/api/campaigns?portfolio=Platinum")
    print("  http://127.0.0.1:5000/api/campaigns?portfolio=Delta")
    print("")
    app.run(debug=True, port=5000)