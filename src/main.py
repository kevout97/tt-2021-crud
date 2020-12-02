from Crud import app
import os


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=int(os.environ['TT_PORT']), debug=True)