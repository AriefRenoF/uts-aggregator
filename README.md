Cara build dan RUN:

Build: docker build -t uts-aggregator .
Run: docker run -p 8080:8080 uts-aggregator

Endpoint:
POST /publish: Mengirim event.
GET /events?topic=...: Mengambil daftar event unik.
GET /stats: Menampilkan statistik.