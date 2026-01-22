from flask import Flask, request, render_template ,redirect ,abort
from markupsafe import escape
app = Flask(__name__)
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
          key_func=get_remote_address,
          default_limits=["200 per second"],
          storage_uri ="memory://"
)
limiter.init_app(app)


@app.route('/limiter')
@limiter.limit("1 per hour")
def limiter_page():
    return get_remote_address()

@app.route('/')
def index():
   #name=request.args.get('name')
   return 'Hello World'  #+ name


@app.route('/redicting')
def redicting():
    return redirect('/',code=302)



@app.get('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


@app.get('/html_templating')
def html_templating():
    return render_template('sample.html',name='sample')

if __name__ == '__main__':
    app.run(debug=True)