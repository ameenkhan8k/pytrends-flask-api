from flask import Flask, jsonify
from pytrends.request import TrendReq

app = Flask(__name__)


@app.route('/trending-topics', methods=['GET'])
def get_trending_topics():
    try:
        pytrends = TrendReq(hl='en-IN', tz=330)
        trending = pytrends.trending_searches(pn='india')
        topics = trending[0].tolist()[:5]

        return jsonify({
            "status": "success",
            "topics": topics
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
