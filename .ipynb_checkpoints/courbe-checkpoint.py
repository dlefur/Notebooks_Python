#-----------------------------------------------
# Module courbe.py permettant d'afficher une courbe
#-----------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

#---------------- pour un affichage automatique 
xmin = -5
xmax = 5

#--------------- réglages utilisés pour un affichage personnalisé
ymin=-5
ymax=30

xstep=1
ystep=5



#------------------------------------------------------
def affichage_automatique(f,nom="$({\cal C}_f$)",couleur="blue"):
  """
  Fonction affichant automatiquement une courbe
  """
  x = np.linspace(xmin,xmax, 1000)
  y = f(x)
  plt.plot(x, y,label=nom, color=couleur, linewidth=2)


#------------------------------------------------------  
def affichage_personnalise(f,nom="$({\cal C}_f$)",couleur="blue") :
  """
  Fonction affichant une courbe personnalisé
  """
  plt.xlim(xmin, xmax)
  plt.ylim(ymin, ymax)

  x = np.linspace(xmin,xmax, 1000)
  y = f(x)
  y = np.ma.masked_less(y, ymin) 
  y = np.ma.masked_greater(y,ymax)
  plt.plot(x, y, label=nom, color=couleur, linewidth=2)

  plt.axhline(0,color="black")
  plt.axvline(0,color="black")

  plt.xticks(np.arange(xmin,xmax+xstep,xstep))
  plt.yticks(np.arange(ymin,ymax+ystep,ystep))


  
#-------------------------------------------------------  
def affichage(f,nom="$({\cal C}_f$)",couleur="blue",auto=1) :
  """
  Fonction permettant de choisir entre les deux affichages
  """
  if (auto==1):
    affichage_automatique(f,nom,couleur)
  else :
    affichage_personnalise(f,nom,couleur)
    

#-------------------------------------------------------  
def asymptote_horizontale(yval,couleur="black",style="--") :
  """
  Fonction traçant une asymptote horizontale
  """
  plt.plot([xmin,xmax],[yval,yval],couleur,linestyle=style,linewidth=2)
  
  
  
#-------------------------------------------------------  
def asymptote_verticale(xval,couleur="black",style="--") :
  """
  Fonction traçant une asymptote verticale
  """
  plt.plot([xval,xval],[ymin,ymax],couleur,linestyle=style,linewidth=2)
    
  

