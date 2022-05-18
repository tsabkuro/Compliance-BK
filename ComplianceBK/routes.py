import os
from flask import render_template, url_for, flash, redirect, request, abort, session
from ComplianceBK import app
from ComplianceBK.forms import ContactForm


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = ContactForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        flash('We will get back to you as soon as possible.')
        return redirect('/home#contact')
    return render_template('home.html', form=form)



# form = ContactForm(request.form)
#     if request.method == 'POST' and form.validate_on_submit():
#         flash('We will get back to you as soon as possible.', 'success')
#         return redirect(url_for('home'))
#     elif request.method == 'POST':
#         flash('One or more fields have an error. Please check and try again.', 'warning')
#         return redirect(url_for('home'))
#     elif request.method == 'GET':
#     	return render_template('home.html', form=form)