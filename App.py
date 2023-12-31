from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.otetubl.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp')
db = client.dbsparta

app = Flask(__name__)

@app.route("/bucket", methods=["POST"])
def bucket_post():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'POST /bucket request!'})

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form["bucket_give"]
    count = db.bucket.count_documents({})
    num = count + 1
    doc = {
        'num':num,
        'bucket': bucket_receive,
        'done':0
    }
    db.bucket.insert_one(doc)
return jsonify({'msg':'data saved!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'POST /bucket/done request!'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    buckets_list = list(db.bucket.find({},{'_id':False}))
    return jsonify({'buckets':buckets_list})

if __name__ == '__main__':
app.run('0.0.0.0', port=5000, debug=True)

