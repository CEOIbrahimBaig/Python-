

                                # Matplotlib Markers 


'''
   You can use the keyword argument marker to emphasize each point with a specified marker:

   Marker	Description
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline
''' 

import numpy as np 
import matplotlib.pyplot as plt


ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'D')

plt.show()


ypoint=np.array([1,2,4])

plt.plot(ypoint,'o:g')  # Marker|line|color

plt.show()    


#plt.plot(data_point_x_axis,date_point_y_axis , Marker|Line|Color , markersize or
#  ms= ,markeredgecolor or mec=' ',markerfacecolor or mfc=' ')

# Default datapoint = y 
# Default marker =No dots  ,it uses lines 
# Default color = Blue 
# Default line = ____
# Default  mec = None 
# Default mfc =Blue 

plt.plot(ypoints, marker = 'o', mec = 'g',ms = 50)

plt.show()
