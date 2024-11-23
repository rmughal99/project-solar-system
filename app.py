from flask import Flask,render_template,url_for,request,redirect
import os
app = Flask(__name__)
picfolder = os.path.join('static','pics')
app.config['UPLOAD_FOLDER'] = picfolder
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/QA', methods=['GET', 'POST'])
def QA():
    if request.method == 'POST':
        
        return redirect(url_for('space'))

    return render_template('QA.html')
   
@app.route('/pioneer')
def pioneer():
	pioneer = os.path.join(app.config['UPLOAD_FOLDER'],'Pioneer.jpg')

	return render_template('pioneer.html',image1 = pioneer)

@app.route('/voyager')
def voyager():
	voyager = os.path.join(app.config['UPLOAD_FOLDER'],'voyager1.png')
	return render_template('voyager.html',image2 = voyager)

@app.route('/WMAP')
def WMAP():
	WMAP = os.path.join(app.config['UPLOAD_FOLDER'],'WMAP.png')
	return render_template('WMAP.html',image3 = WMAP)

@app.route('/spitzer')
def spitzer():
	spitzer = os.path.join(app.config['UPLOAD_FOLDER'],'Spitzer.png')
	return render_template('spitzer.html',image4 = spitzer)

@app.route('/Cassini-Huygens')
def Cassini():
	cassini = os.path.join(app.config['UPLOAD_FOLDER'],'Cassini-Huygens.png')
	return render_template('Cassini-Huygens.html',image5 = cassini)

@app.route('/Chandra')
def Chandra():
	chandra = os.path.join(app.config['UPLOAD_FOLDER'],'Chandra.png')
	return render_template('Chandra.html',image6 = chandra)

@app.route('/Hubble')
def Hubble():
	hubble = os.path.join(app.config['UPLOAD_FOLDER'],'Hubble.png')
	return render_template('Hubble.html', image7 = hubble)

@app.route('/Apollo')
def Apollo():
	apollo= os.path.join(app.config['UPLOAD_FOLDER'],'Apollo.jpg')
	return render_template('Apollo.html',image8  = apollo)


@app.route('/Vikings')
def Vikings():
	vikings= os.path.join(app.config['UPLOAD_FOLDER'],'Viking_spacecraft.jpg')
	return render_template('Vikings.html',image9  = vikings)
   

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

    

