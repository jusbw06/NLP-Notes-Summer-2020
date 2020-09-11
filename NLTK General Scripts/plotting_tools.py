#!/bin/python3

import matplotlib.pyplot as plt

def createPlot(scores, title, labels):
	
	print(len(scores))
	
	#labelc = labels[0]
	#labelr = labels[1]
	
	labelnum = range(0,len(labels[0]))
	
	labelc = [str(e) for e in labelnum]
	labelr = labelc
	

	# for i in range(0,256):
		# row, col = divmod(i, 16)
		# chars[row][col] = chr(i)

	fig, ax = plt.subplots()
	ax.set_title(title)
	ax.set_axis_off()

	table = ax.table(
		cellText=scores,
		rowLabels=labelr,
		colLabels=labelc,
		rowColours=["palegreen"] * len(labelr),
		colColours=["palegreen"] * len(labelc),
		cellColours=[[".95" for c in range(len(labelr))] for r in range(len(labelc))],
		cellLoc='center',
		loc='upper left'
	)

	table.auto_set_font_size(False)
	table.set_fontsize(10)
	#table.set_fontsize(500)
	#fig.tight_layout()
	plt.show()

