from flask import Flask, abort, render_template
from classes import RepositoryCandidates, AppTemplateRenderer as Renderer

app = Flask(__name__)

CANDIDATES_FILE: str = 'candidates.json'

@app.route('/')
def page_index():
    candidates = RepositoryCandidates(CANDIDATES_FILE).get_all()
    if candidates:
        return render_template('list.html', candidates=candidates)
    else:
        abort(404)


@app.route('/candidates/<int:candidate_number>')
def page_per_num(candidate_number: int):

    if candidate := RepositoryCandidates(CANDIDATES_FILE).get_by_id(candidate_number):
        return render_template('card.html', candidate=candidate)
        return Renderer.render_by_id(candidate)
    else:
        abort(404)

@app.route('/skills/<skill>')
def page_per_skills(skill: str):
    if candidates := RepositoryCandidates(CANDIDATES_FILE).get_by_skill(skill):
        return Renderer.render_by_skill(candidates)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(host='127.0.0.2', port=80)

