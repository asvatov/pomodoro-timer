# pomodoro-timer

This is a simple example package. You can visit
[Github-Repo](https://github.com/asvatov/pomodoro-timer)
to watch sources.

My dev scripts loop:
- sudo apt-get purge pomodoro-timer
- sudo rm -rf debian/.debhelper debian/pomodoro-timer debian/debhelper-build-stamp debian/files debian/pomodoro-timer.debhelper.log debian/pomodoro-timer.postinst.debhelper debian/pomodoro-timer.substvars
- dh_virtualenv --python=/usr/bin/python3
- dpkg-buildpackage -us -uc -b
