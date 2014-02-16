import os

from flask import redirect, send_from_directory, request, session, g, flash, url_for, abort, render_template
from jinja2 import Environment, FileSystemLoader

from popi import app, model

template_env = Environment(loader=FileSystemLoader('./popi/templates'))

@app.before_request
def before_request():
    model.init_db_if_needed()

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

@app.route('/', methods=['POST', 'GET'])
def root_page():
    model.init_db_if_needed()
    #model.db_session.add(Device('name', '111111', '112221', 'off'))
    #model.db_session.commit()
    template = template_env.get_template('index.html')
    if request.method == "GET":
        devicedb = model.db_session.query(model.Device).all()
    return template.render(devicedb=devicedb)

@app.route('/settings', methods=['POST', 'GET'])
def settings():
    template = template_env.get_template('settings.html')
    return template.render()

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        hc = str(request.form['hc1']) + str(request.form['hc2']) + str(request.form['hc3']) + str(request.form['hc4']) + str(request.form['hc5'])
        dc = str(request.form['dc1']) + str(request.form['dc2']) + str(request.form['dc3']) + str(request.form['dc4']) + str(request.form['dc5'])
        model.db_session.add(model.Device(name, hc, dc, 0))
        model.db_session.commit()
        return redirect(url_for('root_page'))
    template = template_env.get_template('add.html')
    return template.render()

@app.route('/remove', methods=['POST', 'GET'])
def remove():
    template = template_env.get_template('remove.html')
    if request.method == "GET":
        #model.db_session.delet(model.Device('wwww', '10000', '00000', 0))
        #model.db_session.commit()
        devicedb = model.db_session.query(model.Device).all()
        #devicedb = model.Device.query.filter_by(name='Adrian Wolf').first()
        return template.render(devicedb=devicedb)
    if request.method == "POST":
        device_id = request.form['id']
        device_object = model.Device.query.filter_by(id=device_id).first()
        model.db_session.delete(device_object)
        model.db_session.commit()
        return template.render()


