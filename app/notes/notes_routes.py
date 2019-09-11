from flask import render_template, redirect, request

# coding: utf-8
import os
from flask import (
    Blueprint, request, render_template
)

from models import Note
from app import db

# Blueprint Configuration
notes_blueprint = Blueprint('notes_blueprint', __name__,
                            template_folder='templates',
                            static_folder='static')

@notes_blueprint.route('/')
def index():
    return render_template('index.html')


@notes_blueprint.route('/notes/')
@notes_blueprint.route('/notes/<int:id>')
def notes(id=False):
    if id:
        notas = Note.query.filter_by(id=id).first()
        return render_template('detail_note.html', notas=notas)
    else:
        notas = Note.query.all()
        return render_template("list_notes.html", notas=notas)


@notes_blueprint.route('/notes/excluir/<int:id>')
def excluir(id=False):
    if id:
        nota = Note.query.filter_by(id=id).first()
        db.session.delete(nota)
        db.session.commit()
        return redirect('/notes/')
    else:
        return redirect('/notes/')


@notes_blueprint.route("/notes/editar/<int:id>", methods=["GET", "POST"])
def editar(id=False):
    if request.method == "GET":
        if id:
            nota = Note.query.filter_by(id=id).first()
            if nota:
                return render_template('edit_note.html', form=nota)
            else:
                return redirect('/notes/')
    else:
        if id:
            nota = Note.query.filter_by(id=id).first()
            if nota:
                nota.title = request.form.get('title')
                nota.body = request.form.get('body')
                db.session.commit()
                return redirect('/notes/')
            else:
                return render_template('edit_note.html', form=nota)

@notes_blueprint.route("/notes/create", methods=["GET", "POST"])
def create_note():
    if request.method == "GET":
        return render_template("create_note.html")
    else:
        if request.form['title'] != '' and request.form['body'] != '':
            title = request.form["title"]
            body = request.form["body"]
            note = Note(title=title, body=body)
            db.session.add(note)
            db.session.commit()
            return redirect("/notes/")
        else:
            return render_template('create_note.html')
