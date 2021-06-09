#Evan Petersen -- Anubis Interview
from flask import Flask, render_template, request, session, url_for, redirect, send_file, after_this_request
from werkzeug.utils import secure_filename
import pymysql.cursors
import os

#Initialize
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
app.config['SECRET_KEY'] = 'sorry this took so long >_<'

TEMP_PATH = './tmp/'

#Configuration for MySQL
conn = pymysql.connect(host='localhost',
                        user='root',
                        password='',
                        db='file_server',
                        charset='utf8mb4',
                        cursorclass=pymysql.cursors.DictCursor)

#Display data from the database 
@app.route('/', methods=['GET', 'POST'])
def display():
    cursor = conn.cursor()
    query = 'SELECT * FROM file'
    cursor.execute(query)
    data = cursor.fetchall()
    return render_template('index.html', flist=data)

#For file upload -- Uploads overwrite files of the same name
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    print('Extracting form')
    file = request.files['upload']
    filename = secure_filename(file.filename)
    print('Pulled data: ', filename)
    data = file.read()
    print(filename, ' converted to binary\n')
    cursor = conn.cursor()
    upload = 'INSERT INTO file VALUES(%s, %s, CURRENT_TIMESTAMP, 0)'
    cursor.execute(upload,(filename, data)) 
    conn.commit()
    cursor.close()
    return redirect('/')

#For file download -- will populate the tmp folder, as files cycle out of the database and new ones are brought
#                       in it will result in clutter
@app.route('/download/<filename>', methods=['GET', 'POST'])
def download(filename):
    cursor = conn.cursor()
    query = 'SELECT data FROM file WHERE name=%s'
    cursor.execute(query, (filename))
    datafile = cursor.fetchone()
    path = TEMP_PATH+filename
    #Saves file to tmp folder for transfer
    with open(path, 'wb') as file:
        file.write(datafile['data'])
    #Increment the download count
    query = 'UPDATE file SET downloads=downloads+1 WHERE name=%s'
    cursor.execute(query, (filename))
    #Delete the temp file -- doesn't work with Windows apparently?
    #@after_this_request
    #def remove_file(response):
    #    os.remove(path)
    #    return response
    
    return send_file(path, attachment_filename=filename, as_attachment=True)

#Running on localhost port 1992
if __name__ == "__main__":
    app.run('127.0.0.1', 1992)
