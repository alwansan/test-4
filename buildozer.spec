[app]

# ── معلومات التطبيق ──────────────────────────────────────────────
title           = B-Ultra
package.name    = bultra
package.domain  = org.bultra
version         = 14

# ── الكود المصدري ────────────────────────────────────────────────
source.dir          = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
source.exclude_dirs = .git, .github, .ci, __pycache__, .buildozer

# ── المكتبات ─────────────────────────────────────────────────────
# ملاحظة: yt-dlp يُثبَّت تلقائياً عند أول تشغيل عبر safe_pip في main.py
# (ليس له recipe في p4a لذا نستبعده هنا ونتركه للتثبيت الذاتي)
requirements = python3,flask,requests,certifi,urllib3,charset-normalizer,idna,werkzeug,jinja2,markupsafe,click,itsdangerous,blinker,setuptools

# ── إعدادات Android ──────────────────────────────────────────────
# الحد الأدنى للـ API (Android 7.0)
android.minapi  = 24

# Target API — 34 = Android 14 (متوافق مع Android 15)
android.api     = 34

# NDK API
android.ndk_api = 24

# المعماريات: arm64-v8a للـ Poco F5 Pro + armeabi-v7a للتوافق
android.archs   = arm64-v8a, armeabi-v7a

# قبول تراخيص SDK تلقائياً (ضروري للـ CI)
android.accept_sdk_license = True

# ── الصلاحيات ────────────────────────────────────────────────────
# INTERNET              : للاتصال بالإنترنت
# ACCESS_NETWORK_STATE  : فحص حالة الشبكة
# WRITE_EXTERNAL_STORAGE: الكتابة (Android < 10)
# READ_EXTERNAL_STORAGE : القراءة (Android < 13)
# READ_MEDIA_VIDEO      : قراءة الفيديو (Android 13+)
# READ_MEDIA_AUDIO      : قراءة الصوت (Android 13+)
# READ_MEDIA_IMAGES     : قراءة الصور (Android 13+)
# MANAGE_EXTERNAL_STORAGE: إدارة كل الملفات (للتحميل في Downloads)
# FOREGROUND_SERVICE    : للتحميل في الخلفية
# WAKE_LOCK             : منع إيقاف الشاشة أثناء التحميل
# VIBRATE               : الاهتزاز للإشعارات
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,READ_MEDIA_VIDEO,READ_MEDIA_AUDIO,READ_MEDIA_IMAGES,MANAGE_EXTERNAL_STORAGE,FOREGROUND_SERVICE,WAKE_LOCK,VIBRATE

# requestLegacyExternalStorage لأندرويد 10
android.meta_data = android.requestLegacyExternalStorage:true

# ── خيارات أخرى ──────────────────────────────────────────────────
orientation      = portrait
fullscreen       = 0
android.allow_backup = True

# ── python-for-android / WebView Bootstrap ───────────────────────
# webview = عرض Flask داخل نافذة Android أصيلة
p4a.bootstrap    = webview

# المنفذ الذي يشتغل عليه Flask (8000 كما في main.py)
p4a.port         = 8000

# فرع p4a — master للحصول على أحدث إصلاحات
p4a.branch       = master

[buildozer]

# مستوى التفاصيل: 2 = debug (يُظهر رسائل الترخيص لرؤية المشاكل)
log_level   = 2

# تحذير عند التشغيل كـ root — 0 لإيقافه في CI
warn_on_root = 0
