set terminal pdf
set output "loss_graph.pdf"
set xlabel "Loss %"
set ylabel "RTT ms"
set title "RTT in function of the loss"
plot "result_loss" using 1:($3*1000):4 with yerrorbars title 'RTT'