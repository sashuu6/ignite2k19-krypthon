git status
git add .
set /p commitMessage= "Please Enter Commit A Message :" 
git commit -m "%commitMessage%"
git push origin master
timeout /T 500