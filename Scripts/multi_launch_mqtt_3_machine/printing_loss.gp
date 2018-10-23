set terminal pdf
set output "loss_graph.pdf"
set xlabel "Loss %"
set ylabel "Average RTT ms"
set title "RTT in function of the loss"
set xrange [3:17]
set yrange [0:100]
plot "result_loss" using 1:($3*1000):4 with yerrorbars title 'RTT'