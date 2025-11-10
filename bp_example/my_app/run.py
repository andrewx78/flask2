import os, sys
sys.path.append(os.path.pardir)
from my_app import create_app
from my_app.config import ProductionConfig

#print(app.config) #Default config

app = create_app("prod")

print(app.config.get("SECRET_KEY")) #Словарь настроек для Flask-


if __name__ == '__main__':
    # app.run()
    app.run(port=ProductionConfig.PORT, host=ProductionConfig.SERVER_NAME, debug=ProductionConfig.DEBUG)
