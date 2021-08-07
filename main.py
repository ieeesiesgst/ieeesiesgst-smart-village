from website import create_app
import os

app = create_app()

if __name__ == "__main__":
    app.run(port=os.getenv("PORT", default=5000))
