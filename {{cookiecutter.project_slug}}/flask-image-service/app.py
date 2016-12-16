import base64
import boto3
import calendar
import io
from datetime import datetime, timedelta

from flask import Flask, request, render_template
from PIL import Image


s3 = boto3.resource('s3')
BUCKET_NAME = '{{ cookiecutter.aws_bucket_name }}'
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        new_file_b64 = request.form['b64file']
        if new_file_b64:

            # Decode the image
            new_file = base64.b64decode(new_file_b64)

            # Crop the Image
            img = Image.open(io.BytesIO(new_file))
            img.thumbnail((200, 200))

            # Tag this filename with an expiry time
            future = datetime.utcnow() + timedelta(days=10)
            timestamp = str(calendar.timegm(future.timetuple()))
            filename = "thumb.%s.jpg" % timestamp

            # Send the Bytes to S3
            img_bytes = io.BytesIO()
            img.save(img_bytes, format='JPEG')
            s3_object = s3.Object(BUCKET_NAME, filename)
            resp = s3_object.put(
                Body=img_bytes.getvalue(),
                ContentType='image/jpeg'
                )

            if resp['ResponseMetadata']['HTTPStatusCode'] == 200:

                # Make the result public
                object_acl = s3_object.Acl()
                object_acl.put(ACL='public-read')

                # And return the URL
                object_url = "https://{0}.s3.amazonaws.com/{1}".format(
                    BUCKET_NAME,
                    filename)
                return object_url, 200
            else:
                return "Something went wrong :(", 400

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
