from flask import Flask, send_file, send_from_directory, safe_join, abort
from flask_restx import Api, Resource, reqparse
from werkzeug.datastructures import FileStorage
import io
import os
from PIL import Image

app = Flask(__name__)
api = Api(app)

app.config['DEBUG'] = True

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument("image-upload", type=FileStorage, location='files', help='Please add the file')


@api.route('/file')
class NewAPI(Resource):

    @api.expect(parser)
    def post(self):
        args = parser.parse_args()
        print(args)
        imgup = args.get('image-upload')
        print(imgup)
        save_file_at = os.path.join(app.root_path , 'statics/pics/' ,imgup.filename)
        i = Image.open(imgup)
        i.save(save_file_at)
        return send_file(filename_or_fp=io.BytesIO(imgup.read()), mimetype='image/jpg', as_attachment=True, attachment_filename=imgup.filename)
        
        


if __name__ == '__main__':
    app.run()
