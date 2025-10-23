from flask import Flask, render_template, request, redirect
from DB import get_connection

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM clients ORDER BY id_client ASC;''')
    clients = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', clients=clients)


@app.route('/create', methods=['POST'])
def add():

    conn = get_connection()
    cur = conn.cursor()
    client_name = request.form['name']
    client_email = request.form['email']
    atividade = request.form['atividade']
    cur.execute('''INSERT INTO clients (client_name, client_email, data_cadastro, atividade) VALUES (%s, %s, CURRENT_DATE, %s);''', (client_name, client_email, atividade))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(('/'))


@app.route('/delete', methods=['POST'])
def delete():
    conn = get_connection()
    cur = conn.cursor()
    id_client = request.form['id_client']
    cur.execute('''DELETE FROM clients WHERE id_client=%s;''', (id_client))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)