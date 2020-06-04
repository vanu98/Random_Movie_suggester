from flask import *
import imdb
app = Flask(__name__)
decc1=[]
@app.route('/')
def home():
	return render_template('index.html')

@app .route('/result', methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form
		a = result.values()
		a = list(a)
		code = str(a[0])
		decc1 = imd(code)
		return render_template('result.html', result=decc1)

def imd(code):
	decc2 = []
	ia = imdb.IMDb()
	series = ia.get_movie(code)
	a = series.data['title']
	decc2.append(a)
	year = series.data['series years']
	decc2.append(year)
	return decc2

if __name__ == '__main__':
	app.run(debug = True)