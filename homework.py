from flask import Flask, request
app = Flask(__name__)

case = []
users=dict()

## Main page for our app, we may see it in browser by http://127.0.0.1:5000 URL

@app.route('/all_users', methods=['GET'])
def all_users():
    return users.keys()

@app.route('/all_cases', methods=['GET'])
def all_cases():
    return case

@app.route('/new', methods=['POST'])
def add_case():
    cs1 = request.data.decode('utf-8')
    username=case['username']
    if username not in users:
        users[username]=[]
    users[username].append(cs1)
    case.append(cs1)
    return 'case added'

@app.route('/cases/<username>', methods=['GET'])
def get_user_cases(username):
    if username in users:
        return users[username]
    else:
        return 'user not found'

@app.route('/cases/<username>/<case_id>', methods=['PUT'])
def edit_case(username,event_id):
    cs2=request.data.decode('utf-8')
    if username in users and int(case_id)<len(users[usermane]):
        users[username][int(case_id)] = newCase
        case[int(case_id)]=newCase
        return 'case has been edited'
    else:
        return 'case not found'

@app.route('/cases/<username>/<case_id>', methods=['DELETE'])
def delete_case(username, case_id):
    if username in users and int(case_id) < len(users[usermane]):
        deleteCase=users[username].pop(int(case_id))
        case.remove(deleteCase)
        return 'case has been deleted'
    else:
        return 'case not found'


if __name__ == '__main__':
    app.run(debug=True)

