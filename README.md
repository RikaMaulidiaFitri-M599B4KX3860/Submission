# Bike Sharing Data Visualization Dashboard

Dashboard ini menampilkan berbagai visualisasi data seputar penggunaan sepeda dalam sistem berbagi sepeda (bike-sharing). Anda dapat melihat tren penggunaan sepeda berdasarkan waktu, cuaca, musim, suhu, dan lain-lain.

## Fitur Visualisasi

1. **Total Rentals Over Time**: Grafik garis yang menunjukkan jumlah total penyewaan sepeda per hari.
2. **Rentals by Season**: Grafik batang yang menunjukkan total penyewaan sepeda berdasarkan musim.
3. **Rentals by Weather Situation**: Diagram kotak yang menunjukkan distribusi penyewaan sepeda berdasarkan kondisi cuaca.
4. **Rentals by Hour**: Grafik batang yang menunjukkan rata-rata penyewaan sepeda di setiap jam dalam sehari.
5. **Rentals vs Temperature**: Diagram pencar yang menunjukkan hubungan antara penyewaan sepeda dan suhu.
6. **Correlation Heatmap**: Heatmap yang menampilkan korelasi antara berbagai fitur numerik dalam dataset.

## Cara Menjalankan

Untuk menjalankan dashboard ini, pastikan Anda sudah menginstall semua paket yang diperlukan.

### Prasyarat

Instal `streamlit` dan beberapa paket lain yang dibutuhkan. Anda dapat menginstal semua paket ini menggunakan `pip` dengan perintah berikut:

```bash
pip install pandas plotly seaborn matplotlib streamlit
