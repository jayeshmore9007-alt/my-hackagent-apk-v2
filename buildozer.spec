[app]
title = HackAgent
package.name = hackagent
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,yaml
version = 0.1
requirements = python3,kivy,requests,urllib3,certifi,charset-normalizer,idna
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
