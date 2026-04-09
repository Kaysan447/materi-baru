def sistem_rotasi_log(logs, data_baru, kapasitas_maks):
    """
    TUGAS 1: PURE LIST - DESIGNING A LOG ROTATOR (C6)
    Waktu Pengerjaan Ideal: 25 Menit

    Skenario:
    Anda mendesain sistem "Log Rotation". List 'logs' memiliki kapasitas terbatas.

    Aturan Desain (Constraints):
    1. Jika 'data_baru' SUDAH ADA di dalam 'logs', pindahkan data tersebut ke
       posisi paling AKHIR (sebagai data terbaru).
    2. Jika 'data_baru' BELUM ADA dan 'logs' sudah penuh (mencapai kapasitas_maks),
       hapus data paling LAMA (indeks 0) sebelum menambah data baru ke akhir.
    3. Jika 'data_baru' BELUM ADA dan 'logs' belum penuh, langsung tambah ke akhir.
    4. Kembalikan list hasil rotasi.

    Contoh:
    logs = ["A", "B"], data_baru = "C", kapasitas = 3 -> ["A", "B", "C"]
    logs = ["A", "B", "C"], data_baru = "B", kapasitas = 3 -> ["A", "C", "B"]
    logs = ["A", "B", "C"], data_baru = "D", kapasitas = 3 -> ["B", "C", "D"]
    """

    # Rancang logika Anda di sini
    