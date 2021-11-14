from website import create_app,db
import os

app = create_app()
db.create_all(app=app)

if __name__ == "__main__":
    # app.debug = True
    app.run(port=os.getenv("PORT", default=5000))
