from flask import Flask, request, jsonify, Response
from flask_restx import Api, fields, Resource
from flask_restx.reqparse import RequestParser
from flask_sqlalchemy import SQLAlchemy
from werkzeug.datastructures import FileStorage
from flask_marshmallow import Marshmallow

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

parser = RequestParser(bundle_errors=True)
parser.add_argument('name', help='Name field required', required=True)
parser.add_argument('email')
parser.add_argument('files', type=FileStorage, location='files')

class DB(db.Model):
    __tablename__ = 'db'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), index=True)
    email = db.Column(db.String(35))
    files = db.Column(db.String(100))
    file_data = db.Column(db.LargeBinary)

class DBSchema(ma.Schema):
    class Meta:
        fields = ("id", 'name', 'email', 'files')

db.create_all()
dbschema = DBSchema()
dbschemas = DBSchema(many=True)



@api.route('/A/')
@api.doc({'200'})
class Example(Resource):

    def get(self):
        dbs = DB.query.all()
        return dbschemas.jsonify(dbs)

    @api.expect(parser, validate=True)
    def post(self):
        args = parser.parse_args()
        name = args['name']
        email = args['email']
        files = args['files']
        aps = DB(name=name,email=email,files=files.filename, file_data=files.read())
        db.session.add(aps)
        db.session.commit()
    
@api.route('/A/<int:id>')
class ExampleWithId(Resource):

    def get(self,id):
        dbs = DB.query.filter_by(id=id).first_or_404("Not found")
        file_data = dbs.file_data
        if str(dbs.files).split(".")[1] in ['jpg','jpeg']:
            mimetype='image/jpeg'
        elif str(dbs.files).split(".")[1] == 'mp3':
            mimetype='audio/mpeg'
        elif str(dbs.files).split(".")[1] in ['mp4','mkv']:
            mimetype='audio/mp4'
        elif str(dbs.files).split(".")[1] == 'png':
            mimetype='image/png'
        elif str(dbs.files).split(".")[1] == 'pdf':
            mimetype='application/pdf'
        else:
            mimetype='application/octet-stream'
        #result = app.response_class(file_data, mimetype=mimetype)
        #print(type(result))
        return Response(file_data, mimetype=mimetype)

if __name__ == '__main__':
    app.run(debug=True)