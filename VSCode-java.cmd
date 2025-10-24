@echo off
rem 
rem VsCode portable dla Janusza Stala
rem
rem sparawdzenie poprawności pliku:
rem 7zip.exe t nazwa_pliku_do_sprawdzenia - wynik powinien być pod %errorlevell%
rem
cls
"c:\Program Files\7-Zip\7z.exe" t c:\Drivers\VSCode-java.exe
if %ErrorLevel% NEQ 0 (
 		CLS
		echo Czekaj! Kopiuje pliki.
rem 		copy /Y \\v-kwiryn.campus.uek.krakow.pl\Install\Laboratoria\LabCSI\Install\VSCode\VSCode-java.exe  c:\drivers\VSCode-java.exe
		copy /Y \\10.10.0.3\Laboratoria\Test\VSCode\VSCode-java.exe c:\drivers\VSCode-java.exe
 	) ELSE	(
		CLS
 		echo Plik jest OK.
 			)
rmdir /Q /S %USERPROFILE%\VSCode-java
c:\drivers\VSCode-java.exe -o%USERPROFILE% -y
copy \\v-kwiryn.campus.uek.krakow.pl\Install\Laboratoria\LabCSI\Install\VSCode\VSCode-java.lnk %USERPROFILE%\desktop\VSCode-java.lnk
