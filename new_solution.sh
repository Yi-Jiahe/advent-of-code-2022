#!bin/bash

if [[ -z $1 ]]; then
  echo "Please provide a day"
  exit 1
fi

day=$1

if [ -d "day_${day}" ]; then
  echo "Solution already exists for day ${day}"
  exit 1
fi

cp days/template_day.txt "days/day_${day}.py"
touch "inputs/day_${day}_input.txt"
cp tests/template_test.txt "tests/test_day_${day}.py"
sed -i "s/DAY/${day}/" "tests/test_day_${day}.py"
