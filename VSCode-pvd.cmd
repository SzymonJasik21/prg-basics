@echo off
rem
rem VsCode portable dla Janusza Stala
rem
rem sparawdzenie poprawności pliku:
rem 7zip.exe t nazwa_pliku_do_sprawdzenia - wynik powinien być pod %errorlevell%
rem
cls
"c:\Program Files\7-Zip\7z.exe"  t c:\Drivers\VSCode-pvd.exe
if %ErrorLevel% NEQ 0 (
 		CLS
		echo Czekaj! Kopiuje pliki.
rem 		copy /Y \\v-kwiryn.campus.uek.krakow.pl\Install\Laboratoria\LabCSI\Install\VSCode\VSCode-pvd.exe c:\drivers\VSCode-pvd.exe
 		copy /Y \\10.10.0.3\Laboratoria\Test\VSCode\VSCode-pvd.exe c:\drivers\VSCode-pvd.exe
 	) ELSE	(
		CLS
 		echo Plik jest OK.
 			)
rmdir /Q /S %USERPROFILE%\VSCode-pvd
c:\drivers\VSCode-pvd.exe -o%USERPROFILE% -y
copy \\v-kwiryn.campus.uek.krakow.pl\Install\Laboratoria\LabCSI\Install\VSCode\VSCode-pvd.lnk %USERPROFILE%\desktop\VSCode-pvd.lnk
