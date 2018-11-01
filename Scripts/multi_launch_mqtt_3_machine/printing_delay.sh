set terminal pdf
set output "delay_graph.pdf"
set xlabel "Delay ms"
set ylabel "RTT ms"
set title "RTT in function of the Delay"
plot "result_delay" using 2:($3*1000):4 with yerrorbars title 'RTT'