#!/bin/bash

#mkdir exampleoutput

#preprocessing

start=$(date +%s.%N)

python hed_conversion.py AB04-BCL2.png AB04-BCL2-H.png
python hed_conversion.py AB04-BAX.png AB04-BAX-H.png

end_prepro=$(date +%s.%N)


for i in $(seq 1 23)
do
	avg_time=0
	N=20
	avg_mut_info=0
	avg_rmse=0
	mkdir output$i
	#average results over N executions
	for j in $(seq 1 $N)
	do
		start_elastix=$(date +%s.%N)
		elastix -f AB04-BCL2-H.png -m AB04-BCL2-H-tr.png -out output$i -p parameter_lisa_mod_powell$i.txt #-t0 transform_parameter.txt
		end_elastix=$(date +%s.%N)
		elastix_time=$(echo "$end_elastix - $start_elastix" | bc)
		avg_time=$(echo $avg_time + $elastix_time | bc)
		echo $avg_time
		
		mutinfo=$(python mutual_information.py AB04-BCL2-H.png output$i/result.0.png 2>&1)
		avg_mut_info=$(echo $avg_mut_info + $mutinfo | bc)
		echo $avg_mut_info
		
		rmse=$(python rmse.py AB04-BCL2-H.png output$i/result.0.png 2>&1)
		avg_rmse=$(echo $avg_rmse + $rmse | bc)
		echo $avg_rmse
	done
	
	avg_time=$(echo "scale=5; $avg_time / $N" | bc)
	echo "$i : $avg_time" >> registration_times.txt
	
	avg_mut_info=$(echo "scale=5; $avg_mut_info / $N" | bc)
	echo "$i : $avg_mut_info" >> MI.txt
	
	avg_rmse=$(echo "scale=5; $avg_rmse / $N" | bc)
	echo "$i : $avg_rmse" >> rmse.txt

	python checkerboard_save.py AB04-BCL2-H.png AB04-BCL2-H-tr.png output$i/checkerboard_pattern_1.png
	python checkerboard_save.py AB04-BCL2-H.png output$i/result.0.png output$i/checkerboard_pattern_2.png
done

#prepro_time=$(echo "$end_prepro - $start" | bc)
#elastix_time=$(echo "$end_elastix - $end_prepro" | bc)

#echo "Preprocessing time: $prepro_time"
#echo "Registration time: $elastix_time"

#printf $elastix_time >> registration_times.txt

