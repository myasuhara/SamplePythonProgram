"""
A final project for Python programming class at Foothill in Spring Semester, 2017

Operations: Design the Web API to have the desired operations.

design a REST (Links to an external site.)Links to an external site.
Web API for Basic matrix applications using the Flask (Links to an external site.)
Links to an external site. microframework.

A and B matrix are input data while C matrix is results.

URL Summary:

URL					                    REST PUT/POST
---------------------------------------	---------------------------------------
Hostname/displaymatrix/<matrixname>	    GET
Hostname/all				            GET
Hostname/matrices/<matrixname>		    GET, POST, and DELETE
Hostname/calculations			        GET

Function Summary
def validation: validate input data
def calculations: main control process for calculations
def cal: sub process for calculations

"""
from flask import Flask
from flask import Response
from flask import url_for
from flask import request
from flask import jsonify
from flask import render_template   # callinig to an html file.

app = Flask(__name__)

matrices_dic ={}                    # stores all input data (A and B matrix) and results (C matrix).

status_response = {                 # stores the status of any process.
    "datatype": "status",
    "statusmessage" : "",
    "errorcode":0
}

@app.route('/displaymatrix/<matrixname>', methods=['GET'])  # Display each matrix by showinig with html.
def display_matrix(matrixname):
    if matrixname in matrices_dic.keys():
        results_matrix2 = matrices_dic[matrixname]
        results_matrix3 = results_matrix2["matrixdata"]
        return render_template('index.html', matname=matrixname, name=results_matrix3)

        # calling to 'index.html' storeed in .\templates

    else:
        status_response["statusmessage"] = "a matrix " + matrixname + " does not exist."
        status_response["errorcode"] = 110
        return jsonify(status_response)

@app.route('/all', methods=['GET'])         # shows all data including A, B, and C matrix for valiodation purpose.
def display_all_matrix():
    return jsonify(matrices_dic)

@app.route('/matrices/<matrixname>', methods=['GET', 'POST', 'DELETE'])  # main IO operation function.
def io_matrix(matrixname):
    if request.method == 'GET':
        if matrixname in matrices_dic.keys():
            return jsonify(matrices_dic[matrixname])
        else:
            status_response["statusmessage"] = "a matrix " + matrixname + " does not exist."
            status_response["errorcode"] = 111
            return jsonify(status_response)
    elif request.method == 'POST':
        matrix = request.json
        if validation(matrix) == True:
            matrices_dic[matrix["name"]]=matrix["data"]
            status_response["statusmessage"]= "a matrix " + matrixname + " has been added."
            status_response["errorcode"] = 0
            return jsonify(status_response)
        else:
            return jsonify(status_response)
    elif request.method == 'DELETE':
        if matrixname in matrices_dic:
            del matrices_dic[matrixname]
            status_response["statusmessage"] = "a matrix " + matrixname + " has been deleted."
            status_response["errorcode"] = 0
            return jsonify(status_response)
        else:
            status_response["statusmessage"] = "a matrix " + matrixname + " does not exist."
            status_response["errorcode"] = 112
            return jsonify(status_response)
    else:
        pass

@app.route('/calculations',methods=['POST'])   # main process control.
def process_request():
    request_matrix = request.json
    cal(matrices_dic, request_matrix)
    #print(cal(matrices_dic, request_matrix))
    if status_response["errorcode"] == 0:
        results_matrix2 = matrices_dic['C']
        results_matrix3 = results_matrix2["matrixdata"]
        return jsonify(results_matrix3)
        #return render_template('index.html', name=results_matrix3)
    else:
        return jsonify(status_response)

def validation(matx):   # input data validation
    status_response["errorcode"] = 0

    if (matx["data"]['numrows']) > 100:
        status_response["statusmessage"] = "The row of a data matrix row is more than 100. "
        status_response["errorcode"] = 51
    elif (matx["data"]['numcols']) > 100:
        status_response["statusmessage"] = "The col of a data matrix row is more than 100.  "
        status_response["errorcode"] = 52
    else:
        pass

    if status_response["errorcode"] != 0:
        return False
    else:
        return True

def cal(matrices_dic2, dic_c):

    # calculation  function
    # input : master matrix, C request matrix
    # output : calculation  results

    global status_response
    global matrices_dic

    status_response["errorcode"] = 0

    if "A" in matrices_dic2.keys():
        if "B" in matrices_dic2.keys():
            pass
        else:
            status_response["statusmessage"] = "a matrix " + "B" + " does not exist."
            status_response["errorcode"] = 101
            return jsonify(status_response)
    else:
        status_response["statusmessage"] = "a matrix " + "A" + " does not exist."
        status_response["errorcode"] = 102
        return jsonify(status_response)

    dics_a = matrices_dic2["A"]
    dics_b = matrices_dic2["B"]
    list_a = dics_a['matrixdata']
    list_b = dics_b['matrixdata']
    i_loop = int(dics_a['numrows'])
    k_loop = int(dics_a['numcols'])
    j_loop = int(dics_b['numcols'])

    opeType=dic_c['operationtype']

    w, h = j_loop, k_loop;
    list_c = [[0 for x in range(w)] for y in range(h)]

    if opeType == 'multiplication':
        if (int(dics_a['numcols'])) != (int(dics_b['numrows'])):
            status_response["statusmessage"] = "the col of A does not match with the col of B. "
            status_response["errorcode"] = 103
        else:
            for i in range(i_loop):
                for k in range(k_loop):
                    for j in range(j_loop):
                        x = list_a[i][k] * list_b[k][j]
                        list_c[i][j] = list_c[i][j] + x
            status_response["statusmessage"] = "multiplication process has been done successfully."
    elif opeType == 'addition':
        if ((int(dics_a['numcols'])) == (int(dics_b['numcols']))) and ((int(dics_a['numrows'])) == (int(dics_b['numrows']))):
            for i in range(i_loop):
                for k in range(k_loop):
                    x = list_a[i][k] + list_b[i][k]
                    list_c[i][k] = list_c[i][k] + x
            status_response["statusmessage"] = "addition process has been done successfully."
        else:
            status_response["statusmessage"] = "the col and row between A and B does not match. "
            status_response["errorcode"] = 104
    elif opeType == 'subtraction':
        if ((int(dics_a['numcols'])) == (int(dics_b['numcols']))) and ((int(dics_a['numrows'])) == (int(dics_b['numrows']))):
            for i in range(i_loop):
                for k in range(k_loop):
                    x = list_a[i][k] - list_b[i][k]
                    list_c[i][k] = list_c[i][k] + x
            status_response["statusmessage"] = "subtraction process has been done successfully."
        else:
            status_response["statusmessage"] = "the col and row between A and B does not match. "
            status_response["errorcode"] = 105
    else:
            pass

    matrices_dic2["C"] = {
        "numrows": k_loop,
        "numcols": j_loop,
        "matrixdata": list_c
        }

    matrices_dic=matrices_dic2

    #print(list_c)

    return list_c

if __name__ == '__main__':
    app.run(debug=True)
