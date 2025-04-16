from flask import render_template, request, send_from_directory, redirect, url_for, session
from YT import app, baixados
from YT.forms import FormLink
import yt_dlp
import os

@app.route('/', methods=['GET', 'POST'])
def home():
    form_link = FormLink()
    arquivo_baixado = None

    if form_link.validate_on_submit() and 'botao_submit' in request.form:
        
        link = str(form_link.link.data)
        os.makedirs(baixados, exist_ok=True)

        ydl_opts = {
            'outtmpl': os.path.join(baixados, '%(title)s.%(ext)s'),
            'format': 'best'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(link, download=True)
            arquivo_baixado = os.path.basename(ydl.prepare_filename(info))

        session['arquivo_baixado'] = arquivo_baixado
        return redirect(url_for('baixar_video'))

    return render_template('home.html', form_link=form_link, arquivo_baixado=arquivo_baixado)

@app.route('/baixar-video', methods=['GET', 'POST'])
def baixar_video():
    arquivo_baixado = session.get('arquivo_baixado')
    return render_template('baixar-video.html', arquivo_baixado=arquivo_baixado)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(baixados, filename, as_attachment=True)
