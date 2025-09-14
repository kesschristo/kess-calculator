[app]
# (str) Title of your application
title = Kess Calculator

# (str) Package name
package.name = kesscalculator

# (str) Package domain (unique, like a reverse website)
package.domain = org.kess

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (str) Supported orientation (one of: landscape, portrait, sensor)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions (leave empty for now)
android.permissions = 

# (str) Entry point of your app
entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
