#!/bin/bash
cd $4
touch output_temp.txt
g++ $1 -o run.x
chmod +x run.x
./run.x $2 $4/output_temp.txt
diff $4/output_temp.txt $3
rm run.x output_temp.txt
