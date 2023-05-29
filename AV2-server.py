#Nome: Lucas Silva de Oliveira Ra: 0050018893
import mysql.connector
from flask import Flask
from flask_jsonpify import jsonify

app = Flask(__name__)

@app.route("/lista_paises")
def get_lsita_paises():
    conn = mysql.connector.connect (host=host, user=user, passwd=passwd, port=port, database=database)
    cursor = conn.cursor()
    cursor.execute("select distinct Country from customers order by 1")
    records = cursor.fetchall()
    row_headers=[x[0] for x in cursor.description]
    result = [dict(zip(tuple(row_headers), i)) for i in records]
    jret = jsonify(result)
    conn.close()
    return jret

@app.route("/lista_vendas/<pais>")
def get_lista_vendas(pais):
    conn = mysql.connector.connect (host=host, user=user, passwd=passwd, port=port, database=database)
    cursor = conn.cursor()
    cursor.execute(f"select InvoiceId from invoices where BillingCountry = '{pais}'")
    records = cursor.fetchall()
    row_headers=[x[0] for x in cursor.description]
    result = [dict(zip(tuple(row_headers), i)) for i in records]
    jret = jsonify(result)
    conn.close()
    return jret
    
@app.route("/lista_itemvenda/<id_venda>")
def get_lista_itemvenda(id_venda):
    conn = mysql.connector.connect (host=host, user=user, passwd=passwd, port=port, database=database)
    cursor = conn.cursor()
    cursor.execute(f"select TrackId,Quantity from invoice_items where InvoiceId = '{id_venda}'")
    records = cursor.fetchall()
    row_headers=[x[0] for x in cursor.description]
    result = [dict(zip(tuple(row_headers), i)) for i in records]
    jret = jsonify(result)
    return jret

@app.route("/get_genero/<track_id>")
def get_genero(track_id):
    conn = mysql.connector.connect (host=host, user=user, passwd=passwd, port=port, database=database)
    cursor = conn.cursor()
    cursor.execute(f"SELECT DISTINCT genres.Name FROM (genres \
                                            Inner Join tracks on tracks.GenreId = genres.GenreId)\
                                            Where tracks.TrackId = {track_id}")
                                            
    records = cursor.fetchall()
    row_headers=[x[0] for x in cursor.description]
    result = [dict(zip(tuple(row_headers), i)) for i in records]
    jret = jsonify(result)
    return jret
    

host='teste.c5zehphb1gzr.us-east-1.rds.amazonaws.com'
passwd='12345678'
port=3306
database='chinook'
user='admin'

app.run(host='0.0.0.0', port = '8080', debug=True)