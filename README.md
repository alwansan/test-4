# 🚀 B-Ultra APK Builder via GitHub Actions

يحوّل **B_Ultra_v14.py** (Flask WebApp) إلى APK جاهز للتثبيت على **Poco F5 Pro / Android 15**

---

## 📁 هيكل الملفات

```
bultra_apk/
├── main.py                        ← B_Ultra_v14.py (أنت ترفعه)
├── buildozer.spec                 ← إعدادات البناء
├── .ci/
│   └── patch_main.py             ← يُعدِّل main.py تلقائياً
└── .github/
    └── workflows/
        └── build_apk.yml         ← GitHub Actions
```

---

## 📋 خطوات الاستخدام

### 1. أنشئ Repository جديد على GitHub
- اذهب إلى [github.com/new](https://github.com/new)
- اسمه مثلاً: `bultra-apk`
- اجعله **Public** (مجاني بدون قيود)

### 2. ارفع الملفات

ارفع هذه الملفات بنفس المسارات:

```
main.py                          ← B_Ultra_v14.py مُعاد تسميته
buildozer.spec
.ci/patch_main.py
.github/workflows/build_apk.yml
```

### 3. ابدأ البناء تلقائياً
البناء يبدأ تلقائياً عند رفع الملفات.
أو اضغط: **Actions → Build B-Ultra APK → Run workflow**

### 4. حمّل APK
- اذهب إلى **Actions → آخر run → Artifacts**
- حمّل **B-Ultra-APK.zip**
- فك الضغط → ستجد `*.apk`

---

## ⏱️ الوقت المتوقع

| Run أول | ~35-45 دقيقة (تنزيل SDK+NDK) |
|---------|-------------------------------|
| Runs لاحقة | ~15-20 دقيقة (cache) |

---

## 📱 التثبيت على الهاتف

1. **مصادر غير معروفة**: الإعدادات ← التطبيقات ← وصول خاص ← تثبيت تطبيقات غير معروفة
2. ثبّت APK
3. **إذن التخزين**: الإعدادات ← الخصوصية ← مدير الأذونات ← التخزين ← B-Ultra ← السماح
4. شغّل التطبيق (انتظر 10 ثواني للبدء)
