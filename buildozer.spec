[app]

# (str) Title of your application
title = Kess Calculator

# (str) Package name
package.name = kesscalculator

# (str) Package domain (unique identifier, usually org.yourname)
package.domain = org.kess

# (str) Source code where main.py lives
source.dir = .

# (str) Application versioning
version = 0.1

# (str) The main .py file to launch
source.include_exts = py,png,jpg,kv,atlas

# (str) The application entry point
entrypoint = main.py

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0


[buildozer]

# (str) Log level (1 = error, 2 = warn, 3 = info, 4 = debug, 5 = trace)
log_level = 2

# (int) Target Android API (highest available is best)
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 23b

# (int) Android build tools version
android.build_tools = 33.0.2

# (str) Application format: apk or aab
android.release_artifact = apk

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1
