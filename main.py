from flask import Flask, request, send_file, render_template
import subprocess
import os
import io
import glob
import uuid

app = Flask(__name__)
@app.route('/')
def form():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']

    output_template = os.path.join(os.getcwd(), f"%(title)s-{uuid.uuid4()}.%(ext)s")
    
    try:
        subprocess.run(
            ["yt-dlp", "-x", "--audio-format", "wav", "-o", output_template, url],
            check=True
        )

        downloaded_file = glob.glob(os.path.join(os.getcwd(), "*.wav"))[0]

        with open(downloaded_file, "rb") as audio_file:
            audio_data = io.BytesIO(audio_file.read())
        
        # Remove o arquivo temporário
        os.remove(downloaded_file)

        # Extrai o nome do arquivo para o download sugerido
        download_name = os.path.basename(downloaded_file)

        # Envia o arquivo para download
        audio_data.seek(0)
        return send_file(
            audio_data,
            as_attachment=True,
            download_name=download_name,
            mimetype="audio/wav"
        )
    
    except Exception as e:
        return render_template('error.html', error_message=str(e))

if __name__ == "__main__":
    app.run(debug=True)
