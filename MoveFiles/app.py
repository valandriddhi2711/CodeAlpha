from flask import Flask, render_template, url_for
import os
import shutil

app = Flask(__name__)

# Folder paths
SOURCE_FOLDER = os.path.join('static', 'source_images')
DESTINATION_FOLDER = os.path.join('static', 'jpg_images')

# Create folders if not exist
os.makedirs(SOURCE_FOLDER, exist_ok=True)
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def move_files():
    moved_files = []

    # Move .jpg files
    for filename in os.listdir(SOURCE_FOLDER):
        if filename.lower().endswith('.jpg'):
            src = os.path.join(SOURCE_FOLDER, filename)
            dest = os.path.join(DESTINATION_FOLDER, filename)
            shutil.move(src, dest)

            size_kb = round(os.path.getsize(dest) / 1024, 2)
            image_url = url_for('static', filename=f'jpg_images/{filename}')
            moved_files.append({
                "name": filename,
                "size": f"{size_kb} KB",
                "url": image_url
            })

    if moved_files:
        message = f"✅ {len(moved_files)} .jpg files moved successfully!"
    else:
        message = "⚠️ No .jpg files found in the source folder."

    return render_template('index.html', message=message, moved_files=moved_files)

if __name__ == "__main__":
    app.run(debug=True)
