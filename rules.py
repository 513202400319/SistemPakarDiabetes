def forward_chaining(skor):
    if skor >= 10:
        return "⚠️ Risiko Tinggi Diabetes Mellitus"
    elif skor >= 6:
        return "⚠️ Kemungkinan Diabetes Mellitus"
    else:
        return "✅ Tidak Terindikasi Diabetes Mellitus"