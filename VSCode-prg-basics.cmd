@echo off
rem
rem VsCode portable dla Janusza Stala
rem
rem sparawdzenie poprawności pliku:
rem 7zip.exe t nazwa_pliku_do_sprawdzenia - wynik powinien być pod %errorlevell%
rem
cls
"c:\Program Files\7-Zip\7z.exe"  t c:\Drivers\VSCode-prg-basics-new.exe
if %ErrorLevel% NEQ 0 (
 		CLS
		echo Czekaj! Kopiuje pliki.
rem 		copy /Y \\v-kwiryn.campus.uek.krakow.pl\Install\Laboratoria\LabCSI\Install\VSCode\VSCode-prg-basics-new.exe c:\drivers\VSCode-prg-basics-new.exe
		copy /Y \\10.10.0.3\Laboratoria\Test\VSCode\VSCode-prg-basics-new.exe c:\drivers\VSCode-prg-basics-new.exe
 	) ELSE	(
		CLS
 		echo Plik jest OK.
 			)
rmdir /Q /S %USERPROFILE%\VSCode-prg-basics
c:\drivers\VSCode-prg-basics-new.exe -o%USERPROFILE% -y
copy \\v-kwiryn.campus.uek.krakow.pl\Install\Laboratoria\LabCSI\Install\VSCode\VSCode-prg-basics.lnk %USERPROFILE%\desktop\VSCode-prg-basics.lnk
