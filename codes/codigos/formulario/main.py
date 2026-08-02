# importing the tkinter module
from tkinter import *

#cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

# creating the main window
janela = Tk()
janela.title("dados cam")
janela.geometry("1500x700")
janela.configure(background=co9)


#dividindo janela
frame_cima = Frame(janela, width=1500, height=50, bg=co2, relief="flat")
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=1500, height=650, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

#label cima
app_nome = Label(frame_cima, text="dados camera", anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief="flat")
app_nome.place(x=10, y=20)

#config frame baixo

#fs
l_fs = Label(frame_baixo, text='fs', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_fs.place(x=10, y=10)

e_fs = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_fs.place(x=15, y=40)

#fe
l_fe = Label(frame_baixo, text='fe', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_fe.place(x=10, y=70)

e_fe = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_fe.place(x=15, y=100)

#fN
l_fN = Label(frame_baixo, text='fN', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_fN.place(x=10, y=130)

e_fN = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_fN.place(x=15, y=160)

#sN
l_sN = Label(frame_baixo, text='sN', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_sN.place(x=10, y=190)

e_sN = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_sN.place(x=15, y=220)

#sec
l_sec = Label(frame_baixo, text='sec', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_sec.place(x=10, y=250)

e_sec = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_sec.place(x=15, y=280)

#av
l_av = Label(frame_baixo, text='av', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_av.place(x=10, y=310)

e_av = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_av.place(x=15, y=340)

#pix
l_pix = Label(frame_baixo, text='pix', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_pix.place(x=10, y=380)

e_pix = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_pix.place(x=15, y=410)

#456
l_bmax = Label(frame_baixo, text='bmax', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_bmax.place(x=10, y=450)

e_bmax = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_bmax.place(x=15, y=480)

# 1
l_bN = Label(frame_baixo, text='bN', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_bN.place(x=10, y=520)

e_bN = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_bN.place(x=15, y=550)

#"4934.071289"
l_Lmax = Label(frame_baixo, text='Lmax', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_Lmax.place(x=600, y=520)

e_Lmax = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_Lmax.place(x=605, y=550)

#"-2.763663" 
l_mag = Label(frame_baixo, text='mag', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_mag.place(x=400, y=520)

e_mag = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_mag.place(x=405, y=550)

#"0.014122"
l_cdeg = Label(frame_baixo, text='cdeg', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_cdeg.place(x=200, y=520)

e_cdeg = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cdeg.place(x=205, y=550)


#cdegmax="0.052176" 
l_cdegmax = Label(frame_baixo, text='cdegmax', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_cdegmax.place(x=200, y=450)

e_cdegmax = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cdegmax.place(x=205, y=480)

# io="3" 
l_io = Label(frame_baixo, text='io', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_io.place(x=200, y=380)

e_io = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_io.place(x=205, y=410)

# raP="329.588959"
l_raP = Label(frame_baixo, text='raP', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_raP.place(x=400, y=380)

e_raP = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_raP.place(x=405, y=410)

#  dcP="-51.327591"
l_dcP = Label(frame_baixo, text='dcP', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_dcP.place(x=400, y=450)

e_dcP = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_dcP.place(x=405, y=480)

#	 av1="11.845218"
l_av1 = Label(frame_baixo, text='av1', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_av1.place(x=600, y=450)

e_av1 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_av1.place(x=605, y=480)

#  x1="301.266632"
l_x1 = Label(frame_baixo, text='x1', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_x1.place(x=800, y=450)

e_x1 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_x1.place(x=805, y=480)

# y1="443.763489" 
l_y1 = Label(frame_baixo, text='y1', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_y1.place(x=1000, y=450)

e_y1 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_y1.place(x=1005, y=480)

# x2="340.183441"
l_x2 = Label(frame_baixo, text='x2', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_x2.place(x=800, y=520)

e_x2 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_x2.place(x=805, y=550)

#	 y2="368.330780"
l_y2 = Label(frame_baixo, text='y2', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_y2.place(x=1000, y=520)

e_y2 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_y2.place(x=1005, y=550)

#  az1="236.103333"
l_az1 = Label(frame_baixo, text='az1', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_az1.place(x=1200, y=520)

e_az1 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_az1.place(x=1205, y=550)

# ev1="59.304012" 
l_ev1 = Label(frame_baixo, text='ev1', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')  
l_ev1.place(x=1200, y=450)

e_ev1 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_ev1.place(x=1205, y=480)

# az2="243.929413"
l_az2 = Label(frame_baixo, text='az2', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_az2.place(x=1200, y=10)

e_az2 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_az2.place(x=1205, y=40)

#	 ev2="50.987503" 
l_ev2 = Label(frame_baixo, text='ev2', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_ev2.place(x=1200, y=80)

e_ev2 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_ev2.place(x=1205, y=110)

# azm="240.030136"
l_azm = Label(frame_baixo, text='azm', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_azm.place(x=1200, y=150)

e_azm = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_azm.place(x=1205, y=180)

#  evm="55.628471"
l_evm = Label(frame_baixo, text='evm', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_evm.place(x=1200, y=220)

e_evm = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_evm.place(x=1205, y=250)

#  ra1="127.227783"
l_ra1 = Label(frame_baixo, text='ra1', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_ra1.place(x=1200, y=290)

e_ra1 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_ra1.place(x=1205, y=320)

#	 dc1="-36.507988" 
l_dc1 = Label(frame_baixo, text='dc1', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_dc1.place(x=1200, y=360)

e_dc1 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_dc1.place(x=1205, y=390)

# ra2="116.194801" 
l_ra2 = Label(frame_baixo, text='ra2', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_ra2.place(x=1000, y=10)

e_ra2 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_ra2.place(x=1005, y=40)

# dc2="-33.751816" 
l_dc2 = Label(frame_baixo, text='dc2', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_dc2.place(x=1000, y=80)

e_dc2 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_dc2.place(x=1005, y=110)

# ram="122.176857"
l_ram = Label(frame_baixo, text='ram', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_ram.place(x=1000, y=150)

e_ram = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_ram.place(x=1005, y=180)

#	 dcm="-35.393597"
l_dcm = Label(frame_baixo, text='dcm', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_dcm.place(x=1000, y=220)

e_dcm = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_dcm.place(x=1005, y=250)

#class="J8_DLI" 
l_class = Label(frame_baixo, text='class', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_class.place(x=1000, y=290)

e_class = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_class.place(x=1005, y=320)

# m="0" 
l_m = Label(frame_baixo, text='m', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_m.place(x=1000, y=360)

e_m = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_m.place(x=1005, y=390)

# dr="0.256206"
l_dr = Label(frame_baixo, text='dr', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_dr.place(x=800, y=10)

e_dr = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_dr.place(x=805, y=40)

#	 dv="-27.998259" 
l_dv = Label(frame_baixo, text='dv', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_dv.place(x=800, y=80)

e_dv = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_dv.place(x=805, y=110)

# Vo="21.908772"
l_Vo = Label(frame_baixo, text='Vo', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_Vo.place(x=800, y=150)

e_Vo = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_Vo.place(x=805, y=180)

# lng1="-45.617867"
l_lng1 = Label(frame_baixo, text='lng1', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_lng1.place(x=800, y=220)

e_lng1 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_lng1.place(x=805, y=250)

# lat1="-23.075090"
l_lat1 = Label(frame_baixo, text='lat1', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_lat1.place(x=800, y=290)

e_lat1 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_lat1.place(x=805, y=320)


#	 h1="90.981499" 
l_h1 = Label(frame_baixo, text='h1', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_h1.place(x=800, y=360)

e_h1 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_h1.place(x=805, y=390)

# dist1="104.909836"
l_dist1 = Label(frame_baixo, text='dist1', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_dist1.place(x=600, y=10)

e_dist1 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_dist1.place(x=605, y=40)

#  gd1="52.806244"
l_gd1 = Label(frame_baixo, text='gd1', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_gd1.place(x=600, y=80)

e_gd1 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_gd1.place(x=605, y=110)

#  azL1="269.802643"
l_azL1 = Label(frame_baixo, text='azL1', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_azL1.place(x=600, y=150)

e_azL1 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_azL1.place(x=605, y=180)

#	 evL1="20.532850"
l_evL1 = Label(frame_baixo, text='evL1', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_evL1.place(x=600, y=220)

e_evL1 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_evL1.place(x=605, y=250)

#  lng2="-45.779793" 
l_lng2 = Label(frame_baixo, text='lng2', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_lng2.place(x=600, y=290)

e_lng2 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_lng2.place(x=605, y=320)

# lat2="-23.075521"
l_lat2 = Label(frame_baixo, text='lat2', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_lat2.place(x=600, y=360)

e_lat2 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_lat2.place(x=605, y=390)

#  h2="85.009735"
l_h2 = Label(frame_baixo, text='h2', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_h2.place(x=400, y=10)

e_h2 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_h2.place(x=405, y=40)

#	 dist2="108.390320"
l_dist2 = Label(frame_baixo, text='dist2', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_dist2.place(x=400, y=80)

e_dist2 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_dist2.place(x=405, y=110)

#  gd2="67.244690" 
l_gd2 = Label(frame_baixo, text='gd2', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_gd2.place(x=400, y=150)

e_gd2 = Entry(frame_baixo, width=25, justify='left', relief='solid')    
e_gd2.place(x=405, y=180)

# len="17.617920" 
l_len = Label(frame_baixo, text='len', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_len.place(x=400, y=220)

e_len = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_len.place(x=405, y=250)

# GV="24.558561"
l_GV = Label(frame_baixo, text='GV', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_GV.place(x=400, y=290)

e_GV = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_GV.place(x=405, y=320)

#	 rao="205.260025" 
l_rao = Label(frame_baixo, text='rao', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_rao.place(x=200, y=10)

e_rao = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_rao.place(x=205, y=40)

# dco="-24.292416" 
l_dco = Label(frame_baixo, text='dco', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_dco.place(x=200, y=80)

e_dco = Entry(frame_baixo, width=25, justify='left', relief='solid')    
e_dco.place(x=205, y=110)

# Voo="24.150000"
l_Voo = Label(frame_baixo, text='Voo', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_Voo.place(x=200, y=150)

e_Voo = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_Voo.place(x=205, y=180)

# rat="207.376312"
l_rat = Label(frame_baixo, text='rat', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_rat.place(x=200, y=220)

e_rat = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_rat.place(x=205, y=250)

# dct="-24.234274" 
l_dct = Label(frame_baixo, text='dct', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_dct.place(x=200, y=290)

e_dct = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_dct.place(x=205, y=320)

# memo=""
l_memo = Label(frame_baixo, text='memo', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_memo.place(x=1400, y=520)

e_memo = Entry(frame_baixo, width=10, justify='left', relief='solid')
e_memo.place(x=1405, y=550)

janela.mainloop()

# creating the main window
janela = Tk()
janela.title("dados cam")
janela.geometry("1500x700")
janela.configure(background=co9)


#dividindo janela
frame_cima = Frame(janela, width=1500, height=50, bg=co5, relief="flat")
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=1500, height=650, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

#label cima
app_nome = Label(frame_cima, text="dados camera", anchor=NW, font=('Ivy 13 bold'), bg=co5, fg=co1, relief="flat")
app_nome.place(x=10, y=20)

#config frame baixo

#fs
l_fs = Label(frame_baixo, text='fs', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_fs.place(x=10, y=10)

e_fs = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_fs.place(x=15, y=40)

#tz="0" 
l_tz = Label(frame_baixo, text='tz', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_tz.place(x=10, y=70)

e_tz = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_tz.place(x=15, y=100)

# tme="1.000000" 
l_tme = Label(frame_baixo, text='tme', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_tme.place(x=10, y=130)

e_tme = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_tme.place(x=15, y=160)

# lid="GDOP" 
l_lid = Label(frame_baixo, text='lid', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_lid.place(x=10, y=190)    

e_lid = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_lid.place(x=15, y=220)

# sid="1"
l_sid = Label(frame_baixo, text='sid', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_sid.place(x=10, y=250)

e_sid = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_sid.place(x=15, y=280)

#	 lng="-45.189701" 
l_lng = Label(frame_baixo, text='lng', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_lng.place(x=10, y=310)

e_lng = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_lng.place(x=15, y=340)

# lat="-22.811001"
l_lat = Label(frame_baixo, text='lat', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_lat.place(x=10, y=380)

e_lat = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_lat.place(x=15, y=410)

#  alt="549.000000"
l_alt = Label(frame_baixo, text='alt', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_alt.place(x=10, y=450)

e_alt = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_alt.place(x=15, y=480)

#  cx="720"
l_cx = Label(frame_baixo, text='cx', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_cx.place(x=10, y=520)

e_cx = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cx.place(x=15, y=550)

#	 cy="480" 
l_cy = Label(frame_baixo, text='cy', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_cy.place(x=10, y=590)

e_cy = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cy.place(x=15, y=620)

# fps="29.969999"
l_fps = Label(frame_baixo, text='fps', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_fps.place(x=200, y=10)

e_fps = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_fps.place(x=205, y=40)

#  interlaced="1"
l_interlaced = Label(frame_baixo, text='interlaced', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_interlaced.place(x=200, y=80)

e_interlaced = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_interlaced.place(x=205, y=110)

#  bbf="1"
l_bbf = Label(frame_baixo, text='bbf', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_bbf.place(x=200, y=150)

e_bbf = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_bbf.place(x=205, y=180)

#	 frames="81" 
l_frames = Label(frame_baixo, text='frames', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_frames.place(x=200, y=220)

e_frames = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_frames.place(x=205, y=250)

# head="30" 
l_head = Label(frame_baixo, text='head', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_head.place(x=200, y=290)

e_head = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_head.place(x=205, y=320)

# tail="30" 
l_tail = Label(frame_baixo, text='tail', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_tail.place(x=200, y=360)

e_tail = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_tail.place(x=205, y=390)

# drop="-1"
l_drop = Label(frame_baixo, text='drop', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_drop.place(x=200, y=410)

e_drop = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_drop.place(x=205, y=440)

#	 dlev="27"
l_dlev = Label(frame_baixo, text='dlev', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_dlev.place(x=200, y=450)

e_dlev = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_dlev.place(x=205, y=480)

#  dsize="3"
l_dsize = Label(frame_baixo, text='dsize', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_dsize.place(x=200, y=520)

e_dsize = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_dsize.place(x=205, y=550)

#  sipos="1"
l_sipos = Label(frame_baixo, text='sipos', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_sipos.place(x=200, y=590)

e_sipos = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_sipos.place(x=205, y=620)

#  sisize="15" 
l_sisize = Label(frame_baixo, text='sisize', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_sisize.place(x=400, y=10)

e_sisize = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_sisize.place(x=405, y=40)

#	 trig="1" 
l_trig = Label(frame_baixo, text='trig', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_trig.place(x=400, y=80)

e_trig = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_trig.place(x=405, y=110)

# observer="D._MOURAO" 
l_observer = Label(frame_baixo, text='observer', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_observer.place(x=400, y=150)

e_observer = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_observer.place(x=405, y=180)

# cam="Samsung_SCB-2000" 
l_cam = Label(frame_baixo, text='cam', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_cam.place(x=400, y=220)

e_cam = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cam.place(x=405, y=250)

# lens="Fujinon_F1.3"
l_lens = Label(frame_baixo, text='lens', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_lens.place(x=400, y=290)

e_lens = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_lens.place(x=405, y=320)

#	 cap="Easycap" 
l_cap = Label(frame_baixo, text='cap', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_cap.place(x=400, y=360)

e_cap = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_cap.place(x=405, y=390)

# u2="224" 
l_u2 = Label(frame_baixo, text='u2', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_u2.place(x=10, y=450)

e_u2 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_u2.place(x=15, y=480)

# ua="244" 
l_ua = Label(frame_baixo, text='ua', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_ua.place(x=10, y=520)

e_ua = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_ua.place(x=15, y=550)

# memo=""
l_memo = Label(frame_baixo, text='memo', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_memo.place(x=10, y=590)

e_memo = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_memo.place(x=15, y=620)

#	 az="246.714508" 
l_az = Label(frame_baixo, text='az', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_az.place(x=200, y=10)

e_az = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_az.place(x=205, y=40)

# ev="38.911907" 
l_ev = Label(frame_baixo, text='ev', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_ev.place(x=200, y=80)

e_ev = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_ev.place(x=205, y=110)

# rot="1.576300"
l_rot = Label(frame_baixo, text='rot', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_rot.place(x=200, y=150)

e_rot = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_rot.place(x=205, y=180)

#  vx="84.067596"
l_vx = Label(frame_baixo, text='vx', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_vx.place(x=200, y=220)

e_vx = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_vx.place(x=205, y=250)

#	 yx="1.099011"
l_yx = Label(frame_baixo, text='yx', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_yx.place(x=200, y=290)

e_yx = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_yx.place(x=205, y=320)

#  dx="0.926617" 
l_dx = Label(frame_baixo, text='dx', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_dx.place(x=200, y=360)

e_dx = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_dx.place(x=205, y=390)

# dy="19.795353"
l_dy = Label(frame_baixo, text='dy', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_dy.place(x=400, y=10)

e_dy = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_dy.place(x=405, y=40)

#  k4="0.000000"
l_k4 = Label(frame_baixo, text='k4', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_k4.place(x=400, y=80)

e_k4 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_k4.place(x=405, y=110)

#	 k3="-0.068897" 
l_k3 = Label(frame_baixo, text='k3', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_k3.place(x=400, y=150)

e_k3 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_k3.place(x=405, y=180)

# k2="0.017883" 
l_k2 = Label(frame_baixo, text='k2', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_k2.place(x=400, y=220)

e_k2 = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_k2.place(x=405, y=250)

# atc="58.299999" 
l_atc = Label(frame_baixo, text='atc', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_atc.place(x=400, y=290)

e_atc = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_atc.place(x=405, y=320)

# BVF="-0.300000"
l_BVF = Label(frame_baixo, text='BVF', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_BVF.place(x=400, y=360)

e_BVF = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_BVF.place(x=405, y=390)

#	 maxLev="255" 
l_maxLev = Label(frame_baixo, text='maxLev', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_maxLev.place(x=600, y=10)

e_maxLev = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_maxLev.place(x=605, y=40)

# maxMag="0.453000"
l_maxMag = Label(frame_baixo, text='maxMag', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_maxMag.place(x=600, y=80)

e_maxMag = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_maxMag.place(x=605, y=110)

#  minLev="9"
l_minLev = Label(frame_baixo, text='minLev', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_minLev.place(x=600, y=150)

e_minLev = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_minLev.place(x=605, y=180)

#  mimMag="4.000000"
l_mimMag = Label(frame_baixo, text='mimMag', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_mimMag.place(x=600, y=220)

e_mimMag = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_mimMag.place(x=605, y=250)

#	 dl="39" 
l_dl = Label(frame_baixo, text='dl', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_dl.place(x=600, y=290)

e_dl = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_dl.place(x=605, y=320)

# leap="50" 
l_leap = Label(frame_baixo, text='leap', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_leap.place(x=600, y=360)

e_leap = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_leap.place(x=605, y=390)

# pixs="277" 
l_pixs = Label(frame_baixo, text='pixs', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_pixs.place(x=800, y=10)

e_pixs = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_pixs.place(x=805, y=40)

# rstar="23"    
l_rstar = Label(frame_baixo, text='rstar', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_rstar.place(x=800, y=80)

e_rstar = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_rstar.place(x=805, y=110)

#	 ddega="0.024780"
l_ddega = Label(frame_baixo, text='ddega', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_ddega.place(x=800, y=150)

e_ddega = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_ddega.place(x=805, y=180)

#  ddegm="0.043049" 
l_ddegm = Label(frame_baixo, text='ddegm', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_ddegm.place(x=800, y=220)

e_ddegm = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_ddegm.place(x=805, y=250)

# errm="0.756155"
l_errm = Label(frame_baixo, text='errm', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_errm.place(x=800, y=290)

e_errm = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_errm.place(x=805, y=320)

#  Lmrgn="5"    
l_Lmrgn = Label(frame_baixo, text='Lmrgn', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_Lmrgn.place(x=800, y=360)

e_Lmrgn = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_Lmrgn.place(x=805, y=390)

#	 Rmrgn="5" 
l_Rmrgn = Label(frame_baixo, text='Rmrgn', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_Rmrgn.place(x=1000, y=10)

e_Rmrgn = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_Rmrgn.place(x=1005, y=40)

# Dmrgn="5" 
l_Dmrgn = Label(frame_baixo, text='Dmrgn', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_Dmrgn.place(x=1000, y=80)

e_Dmrgn = Entry(frame_baixo, width=25, justify='left', relief='solid')
e_Dmrgn.place(x=1005, y=110)

# Umrgn="5"
l_Umrgn = Label(frame_baixo, text='Umrgn', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_Umrgn.place(x=1000, y=150)

e_Umrgn = Entry(frame_baixo, width=25, justify='left', relief='solid')  
e_Umrgn.place(x=1005, y=180)

janela.mainloop()