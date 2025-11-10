import os, sys
sys.path.append(os.path.pardir)
from my_app import app
#from config import DevelopmentConfig

# print(app.config) #Default config


#app.config.from_object("config.DevelopmentConfig")
#print("\n ========= After loading config ====== \n")
#print(app.config) #Словарь настроек для Flask-

if __name__ == '__main__':
    app.run()
    #app.run(port=DevelopmentConfig.PORT, host=DevelopmentConfig.SERVER_NAME, debug=DevelopmentConfig.DEBUG)
