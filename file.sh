echo "Write user"
read x
adduser $x
echo "Group"
read g

if [ "$g" = "teachers" ]; then
    adduser $x teachers
fi
if [ "$g" = "students" ]; then
    adduser $x students
fi
