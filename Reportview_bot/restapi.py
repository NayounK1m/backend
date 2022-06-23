from pickletools import read_string1
from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)
class CreateUser(Resource):
    def post(self):
        try:
            #입력 파라미터를 설정
            parser = reqparse.RequestParser()
            #필수 매개변수
            parser.add_argument('tent_1', type=str)
            parser.add_argument('tent_2', type=str)
            parser.add_argument('tent_3', type=str)
            parser.add_argument('tent_4', type=str)
            #입력 파싱
            args = parser.parse_args() 
            _tent_1 = args['tent_1']
            _tent_2 = args['tent_2']
            _tent_3 = args['tent_3']
            _tent_4 = args['tent_4']
            
            f=open("./testing.txt",'w')
    
            content={'tent_1': args['tent_1'], 'tent_2': args['tent_2'],
                     'tent_3': args['tent_3'], 'tent_4': args['tent_4']}
            f.write(content['tent_1']+'\n')
            f.write(content['tent_2']+'\n')
            f.write(content['tent_3']+'\n')
            f.write(content['tent_4']+'\n')
            
            f.close()

            #성공값 출력
            return {'StatusCode': '200', 'Message': '저장 성공!'}

        #에러메세지 출력
        except Exception as e:
            return {'error': str(e)}

#http://localhost:8080/report
api.add_resource(CreateUser, '/report')

#flask ip, port 설정
if __name__ ==  '__main__':
    app.run(
    host="localhost",
    port=8080)
