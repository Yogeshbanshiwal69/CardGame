from flask import Flask , render_template,request,redirect,url_for
app=Flask(__name__)
data=[['#','NOTE']]



@app.route('/')
def add():
    return render_template('add.html')
@app.route('/',methods=['POST'])
def add_1():
    if request.method=='POST':
        try:
            task=request.form['text']
            data.append(['*',task])
        except:pass
        try:
            button=request.form['a_button']
            if button=='delete':
                return redirect(url_for('delete'))
            elif button=='edit':
                return redirect(url_for('edit'))
        except:pass
    return render_template('add.html', data=data)



@app.route('/edit')
def edit():
    return render_template('edit.html',data=data)
@app.route('/edit',methods=['POST'])
def edit_1():
    global ctr
    if request.method=='POST':
        try:
            no,note=(request.form['note']).split(",")
            no=int(no)
            data[no]=['*',note]
        except:pass
        try:
            button=request.form['a_button']
            if button=='delete':
                return redirect(url_for('delete'))
            elif button=='add':
                return redirect(url_for('add'))
        except:pass
    return render_template('edit.html', data=data)




@app.route('/delete')
def delete():
    return render_template('delete.html',data=data)
@app.route('/delete',methods=['POST'])
def delete_1():
    global ctr
    if request.method=='POST':
        try:
            no=int(request.form['no'])
            del data[no]
        except:pass
        try:
            button=request.form['a_button']
            if button=='add':
                return redirect(url_for('add'))
            elif button=='edit':
                return redirect(url_for('edit'))
        except:pass
    return render_template('delete.html', data=data)




if __name__ == "__main__" :
    app.run(debug=True)
