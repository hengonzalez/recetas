from app_recetas import app # import app from application.py
from app_recetas.controllers import routes

if __name__ == '__main__': # if this file is run directly, run the app
    app.run(debug=True)  # run the app in debug mode