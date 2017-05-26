from multiprocessing import Process
import os
import time

def run_proc(id):
	os.system(PROCS[int(id)][2])

PROCS = [
	# example of process to be run
	['echo', '/bin/echo']
]

def main():
	proclst = []
	for i in range(len(PROCS)):
		proclst.append(Process(target=run_proc, 
			name='PC5_child_{}'.format(PROCS[i][1]),
			args=str(i)))
		proclst[-1].start()

	while True:
		for i in range(len(proclst)):
			if not proclst[i].is_alive():
				proclst[i].run()


if __name__ == '__main__':
	main()