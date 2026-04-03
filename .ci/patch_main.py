import os

FILE_PATH = "main.py"

# كود لإصلاح شهادات SSL في أندرويد حتى يعمل yt-dlp و requests بدون أخطاء
SSL_FIX_CODE = '''# --- INJECTED BY CI PATCH FOR ANDROID SSL FIX ---
import os
import ssl
try:
    import certifi
    os.environ['SSL_CERT_FILE'] = certifi.where()
    os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
except ImportError:
    pass
ssl._create_default_https_context = ssl._create_unverified_context
# ------------------------------------------------\n
'''

if os.path.exists(FILE_PATH):
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        original_code = f.read()
    
    # التأكد من عدم إضافة الكود مرتين
    if "INJECTED BY CI PATCH" not in original_code:
        with open(FILE_PATH, 'w', encoding='utf-8') as f:
            f.write(SSL_FIX_CODE + original_code)
        print("✅ Successfully patched main.py for Android SSL compatibility.")
    else:
        print("⚡ main.py is already patched.")
else:
    print(f"❌ Error: {FILE_PATH} not found!")
