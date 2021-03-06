import os
import switch
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
    template = template_env.get_template('index.html')
    if request.method == 'GET':
        devicedb = model.db_session.query(model.Device).all()
        return template.render(devicedb=devicedb)
    if request.method == 'POST':
        device_id = request.form['id']
        device_status = request.form['status']
        device_object = model.Device.query.filter_by(id=device_id).first()
        device_object.device_status = device_status
        model.db_session.commit()
        device = switch.RemoteSwitch(unit_code=int(device_object.device_code), system_code=[int(i) for i in str(device_object.home_code)], pin=17)
        if device_object.device_status == 0:
            device.switchOff()
        if device_object.device_status == 1:
            device.switchOn()
        return template.render()

@app.route('/settings', methods=['POST', 'GET'])
def settings():
    template = template_env.get_template('settings.html')
    return template.render()

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        dt = request.form['type']
        hc = str(request.form['hc1']) + str(request.form['hc2']) + str(request.form['hc3']) + str(request.form['hc4']) + str(request.form['hc5'])
        dc = str(request.form['dc'])
        model.db_session.add(model.Device(name, hc, dc, 0, dt))
        model.db_session.commit()
        return redirect(url_for('root_page'))
    template = template_env.get_template('add.html')
    return template.render()

@app.route('/remove', methods=['POST', 'GET'])
def remove():
    template = template_env.get_template('remove.html')
    if request.method == "GET":
        devicedb = model.db_session.query(model.Device).all()
        return template.render(devicedb=devicedb)
    if request.method == "POST":
        device_id = request.form['id']
        device_object = model.Device.query.filter_by(id=device_id).first()
        model.db_session.delete(device_object)
        model.db_session.commit()
        return template.render()

@app.route('/edit', methods=['POST', 'GET'])
def edit():
    template = template_env.get_template('edit.html')
    if request.method == "GET":
        devicedb = model.db_session.query(model.Device).all()
        return template.render(devicedb=devicedb)
    if request.method == "POST":
        device_id = request.form['id']
        name = request.form['name']
        home_code = request.form['hc']
        device_code = request.form['dc']
        device_type = request.form['dt']
        device_object = model.Device.query.filter_by(id=device_id).first()
        device_object.name = name
        device_object.home_code = home_code
        device_object.device_code = device_code
        device_object.device_type = device_type
        model.db_session.commit()
        return template.render()
