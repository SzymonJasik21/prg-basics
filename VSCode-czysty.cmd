@echo off
rem
rem czysty VsCode portable
rem
rem sparawdzenie poprawności pliku:
rem 7zip.exe t nazwa_pliku_do_sprawdzenia - wynik powinien być pod %errorlevell%
rem
cls
"c:\Program Files\7-Zip\7z.exe"  t c:\Drivers\VSCode-czysty.exe
if %ErrorLevel% NEQ 0 (
 		CLS
		echo Czekaj! Kopiuje pliki.
rem 		copy /Y \\v-kwiryn.campus.uek.krakow.pl\Install\Laboratoria\LabCSI\Install\VSCode\VSCode-czysty.exe c:\drivers\VSCode-czysty.exe
		copy /Y \\10.10.0.3\Laboratoria\Test\VSCode\VSCode-czysty.exe c:\drivers\VSCode-czysty.exe
 	) ELSE	(
		CLS
 		echo Plik jest OK.
 			)
rmdir /Q /S %USERPROFILE%\VSCode
c:\drivers\VSCode-czysty.exe -o%USERPROFILE% -y
rem --wymaga podniesienia uprzwnien ???? ----mklink "%USERPROFILE%\Desktop\VSCode-czysty" "d:\ESET----Pakiety biznesowe ESET_2025.pdf" 
copy \\v-kwiryn.campus.uek.krakow.pl\Install\Laboratoria\LabCSI\Install\VSCode\VSCode-czysty.lnk %USERPROFILE%\desktop\VSCode.lnk
start "" %USERPROFILE%\desktop\VSCode.lnk
