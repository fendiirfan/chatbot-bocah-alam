# Ambil image dari Python 3.9 sebagai base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_SERVER_ENABLE_CORS=false

# Membuat direktori kerja untuk aplikasi
WORKDIR /app

# Salin file requirements.txt ke dalam container
COPY requirements.txt .

# Install dependensi yang dibutuhkan
RUN pip install -r requirements.txt

# Salin seluruh kode aplikasi ke dalam container
COPY . .

# Jalankan perintah untuk menjalankan aplikasi Streamlit
CMD streamlit run --server.port $STREAMLIT_SERVER_PORT --server.headless $STREAMLIT_SERVER_HEADLESS --server.enableCORS $STREAMLIT_SERVER_ENABLE_CORS app.py
