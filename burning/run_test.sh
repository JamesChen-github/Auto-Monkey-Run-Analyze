# echo $(dirname "$0")
# python.exe $(dirname "$0")/prepare_case.py $1 $2
# ipython.exe $(dirname "$0")/run_monkey_test.ipy


# . ~/ipythonrc
echo $PATH

# echo $1 $2 $3
echo 'run_test.sh: start prepare_case.py'
python.exe D:/files/test/daily_test/burning/prepare_case.py $1 $2 $3
echo 'run_test.sh: start run_monkey_test.ipy'
ipython.exe D:/files/test/daily_test/burning/run_monkey_test.ipy
echo 'run_test.sh: finish'

# echo 'end python script'
# exit 0
