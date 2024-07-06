python.exe -m nuitka    ^
--standalone    ^
--mingw64   ^
--enable-plugin=pyside6 ^
--windows-console-mode=disable  ^
--windows-icon-from-ico=./favicon.ico ^
--remove-output ^
--onefile   ^
--output-dir=D:\ ^
--output-filename=FakeData ^
main.py