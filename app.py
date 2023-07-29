from main import app


if __name__ == '__main__':
    app.secret_key = 'sec key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True,port=2003, use_reloader=False)