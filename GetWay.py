from flask import Flask,request
import json

app = Flask(__name__)


@app.route("/test_1.0",methods=["GET"])
def check():
   
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
   
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict,ensure_ascii=False)

    get_data = request.args.to_dict()
    name = get_data.get('name')
    age = get_data.get('age')

    return_dict['result'] = tt(name,age)

    return json.dumps(return_dict,ensure_ascii=False)

def tt(name, age):
    result_str = "%sXX%sX" % (name, age)
    return result_str
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
