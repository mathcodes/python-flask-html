# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    # Connect to database and fetch all notes
    conn = sqlite3.connect('data/notes.db')
    c = conn.cursor()
    c.execute('SELECT * FROM notes')
    notes = c.fetchall()
    conn.close()

    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        # Get form data and insert new note into database
        title = request.form['title']
        content = request.form['content']
        conn = sqlite3.connect('data/notes.db')
        c = conn.cursor()
        c.execute('INSERT INTO notes (title, content) VALUES (?, ?)', (title, content))
        conn.commit()
        conn.close()

        flash('Note added successfully!')
        return redirect(url_for('index'))

    return render_template('add_note.html')

@app.route('/edit_note/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    if request.method == 'POST':
        # Get form data and update note in database
        title = request.form['title']
        content = request.form['content']
        conn = sqlite3.connect('data/notes.db')
        c = conn.cursor()
        c.execute('UPDATE notes SET title = ?, content = ? WHERE id = ?', (title, content, id))
        conn.commit()
        conn.close()

        flash('Note updated successfully!')
        return redirect(url_for('index'))

    # Connect to database and fetch note with specified ID
    conn = sqlite3.connect('data/notes.db')
    c = conn.cursor()
    c.execute('SELECT * FROM notes WHERE id = ?', (id,))
    note = c.fetchone()
    conn.close()

    return render_template('edit_note.html', note=note)

if __name__ == '__main__':
    app.run(debug=True)
