#引入
from tkinter import *
import base64
import os
import tkinter.ttk as ttk

#窗口
window=Tk()
window.title("标题")
window.geometry("900x650+600+400")
window.minsize(290,140)
window['background']="yellow"
#图标(内
class Icon(object):           #.ico文件转.py
	def __init__(self):
		self.img='AAABAAEAMDAAAAEAIACoJQAAFgAAACgAAAAwAAAAYAAAAAEAIAAAAAAAACQAAAAAAAAAAAAAAAAAAAAAAAD++/z//vv8//77/P/++/z//vv8//77/P/++/z//fv8//77/P/++/z//vv8//77/P/++/z//fv8//z7/P/7+/z//fv8//z7/P/++/z//fv8//77/P/++/z//vv8//77/P/++/z//fv8//77/P/9+/z/+/r6/+ji2v/d1Mf/9fPv//37/f/++/3//fv8//77/P/++/z//vv9//37/f/W08j/q6WR/6WbhP+flX7/lYxz/8vGuv/7+/z//fv8//37/P/9+vz//vv8//36/f/++/3//fr9//36/P/9+v3//fr9//36/P/9+vz//fr8//36/P/9+vz/5uLg/7Gonv+onpD/n5eG/6WejP/q6OP//fr9//37/f/9+v3//fr9//36/f/9+v3//fr9//37/P/59vX/0LqZ/5JfE/+CUQj/gVcc/9fOwP/+/Pz//fr9//36/f/9+/z//fv7/8fCtP/S0MT/9fPw/9rUzP/f29T/+Pf0/7ermf+mnIf//Pr8//77/f/++/3/8/H2/zAwfv/Lydz//vv9//77/f/++/3//vv9//77/f/++/3//vv8//36/P/OycT/ycK7//f19//q6PD/8/L2/+fm4/+Ti3b/xsO2//37/f/++/3//vv9//77/f/++/3//vv9//r6/f/l0rX/xZNI/9G3iv/czbP/nXc6/4pfIf/59vT//vv9//77/f/9+/z/2dXI/+bm3//Kspb/h1gZ/3pKBf9rPwX/dlQw/83Gv/+5tKb/sqqY//77/f/++/3/4uLw/z0/oP+qps///vv9//77/f/++/3//fr9//77/f/++/3//fr9/9nV1P/c29b/qqbO/y0piv8MB3H/EA5m/2Njkf/p6ez/lpF7/9bUzP/++/3//fr9//76/f/++vz//fr9//n6+v/ku4T/3LBk//37/P/9+vz/6ODO/41YCP/g1sf//fr9//76/f/59vX/1tPH/9i8lf/GgA3/0IsN/8iDCf+tbQT/hE4E/2A+Ef/X0sz/lYxv/+zo5f/9+v3/4+Lx/0NCu/+rqNn//vv8//77/P/++/z//fv8//36/f/++v3/+vf4/9DMy/+gnNr/Fg6+/xMOyv8SDcL/DAij/wQCdf81NHH/6ujs/4iBaP/8+vr//vv9//36/P/9+v3//vv9//ny6f/sumf/79Sf//36/P/9+vz/+vv7/8uxhv/z7+r//fr9//37/P/c2M//8unb/+qcHP/4pBT/+aUU//ikEv/nlQ3/uHEG/3tJA/92XTv/2NTK/6qijv/9+vz/4uL0/0ZE0P+rq+H//fv8//38/P/8+/r//fv8//77/P/++v3/29bV/97d7/8jG+j/GBT5/xkV+P8bFvf/FxHc/w4Iqf8GAm3/fHqg/7Ovn//RzcP//vv8//77/f/++/3//vv9//fu3//yv1//99yr//36/P/9+vz//fv9//77/f/9+/z//vv9//37/f/f2tH/9NGO//SmFv/5pxb/+6YT//umFP/5phT/348K/6FkBP9gOAP/39rT/4yCZv/9+vz/4uL1/0hE5f8eHc7/JCGy/yEgjv/GxNr//fv8//77/f/9+v3/3dfW/5CO8P8XFfX/FxP8/xoU/f8bFvv/Ghb4/xQO1v8KBZH/GBZl/+Ti4P+dln7//fr8//77/f/++/3//vv9//n06v/xvF3/9tea//36/f/++/z//fr7/+vcwv/8+fj//fr9//77/P/f3NP/8dCS//PZm//6szX//aob//unFP/6pxX/8aAQ/7t0B/9xRAL/uaud/5GKcf/9+vz/4uP2/0pH8P9hYOf/iYjX/4eHyP/o5u7//fv8//36/P/9+vz/3dfU/4uG7/+Tj/P/PDT6/yEc+v8aFf3/GRX7/xgS6/8PB6z/BAJn/87L1/+Mh2r//vr9//36/f/9+vz//fr8//37+//uyIL/8r9b//v7+v/++/3/9OnS/9uOD//t4s7//fr8//77/P/e29H/8sZu//ffpf/6zn7//LdB//yoFf/6pxX/96QS/8mAC/9/Twb/rJuI/5SIa//9+vz/4+P2/0pI8f+uq/b//vv9//77/f/++/3//vr9//77/f/9+vz/3tvU/2xm7v+knvT/gHv4/0E7+v8bFP3/GBT9/xkV9v8RCr//BwN2/7i1x/+PiG///fv9//77/P/++/z//fr8//v7/P/y4Ln/7rpX//HMhP/z4Lf/8rJC/+igKv/5+PL//vv9//77/P/h3NL/9Nij//n15f/84aT/+sZR//myIP/3uyb/9cIs/9ymHf+DVAT/saOQ/5GHbf/9+/z/4+T1/01J8P+LhPL/yMT0/8XC6//c2+7//vv8//77/f/8+vz/4NvY/52X7f/k5Pj/nZr4/1hQ/P8sIfz/Mi37/zky9/8mG9f/BQN1/8G/z/+RiG///fr9//77/P/++/z//fr9//v6+//6+vT/8N6w/+3Ccf/1phT/868u//XmxP/9+vz//fr9//37/f/f287/9NWb//jy2v/86Ir/++Vj//vlX//75mj/++Nm//rZT/+bbxX/0sm8/5GGbf/7+vv/7e/4/3Br4v9fWvD/Xlrs/1lU1P9RS7b//fr8//36/P/9+/z/3dfW/5iV7P/g3fb/jIT8/3Bn+v9qY/r/dHL5/3Bt+P9bTff/FA6D/9/d4f+ZkHz//fr8//36/P/9+vz//fr8//PixP/dpET/+Pn1//fx4P/269D/+vnw//v7/f/9+vz//fr8//37/f/a2Mj/8+K+//Tju//24WT/++Zp//3oh//965f//emU//zeev+geTb/5ODa/6GYgf9KStD/rKvc/+Dh9v/X1/P/1tfy/9bU8f/p5fX//fv8//77/P/9+/z/1NLQ/7i37/+4tvH/bWL0/3px+v+Vj/r/pKD2/5yW+f98c/b/Uk2d/8TBtf/Ev7P//vv9//77/P/++/z//vv8//fr0v/vv2X/+/n3//z6/f/9+v3//fr9//76/f/++/z//vv8//77/P/08u3/2tnK/+zNi//z5pX/+uiG//3vsf/+8cT//O+//+PMiv/FtJv/pZqE/+Le1/89OO//qKPs//36+//9+vv//Pv7//76+//++v3//fr9//77/f/++/z/9PHw/9HQzf9/fOf/o5zx/5eO+P/Bufj/1Mv5/8e/+f9uZ8j/x8TZ/4uDbf/39fT//fv9//77/f/++/3//fv9//z7/P/7+/r//Pr8//77/f/++/3//fv9//77/f/++/3//fv9//77/f/9+v3/y8u3/+zo2P/r0Ir/9Oul//r02P/89+r/5tvD/8aykP/V0cb/oJd///37/P/19/j/+/r6//37/f/9+vz//fr9//36/P/9+v3//fr9//36/P/9+vz//fr9/83Kw//a2eT/fnvo/6Kb7//d2/j/6uz3/52Zzv+uq9D/sayc/7+6rv/9+v3//fr9//36/f/9+v3//fr9//36/f/9+v3//fr9//36/f/9+v3//fr9//36/f/9+v3//fr9//36/f/9+v3//Pn5/7i1o//n5dr/28WX/7GBPv+ebTv/tqWS/9HOxP+Ngmb/9vX0//36/f/9+/z//vr9//77/P/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vr8//35/P+/urL/393b/4+M1v8dGab/EhGE/7u40f+wqJr/qZ2O//36/P/++vz//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//Pv8//v6+/+0r53/sqOO/9qHJP+1Wwb/nYpw/5eNcv/39vb//fr8//77/f/++/3//vv8//76/f/9+v3//vv9//77/f/++/3//fr9//77/f/++/3//vr8//36/P/7/Pz/ta2e/46GoP88NN3/BwS6/4R7fP+6saL/+/v8//37/P/++vz//fr9//76/f/++vz//fr9//76/f/++vz//fr9//76/f/++vz//fr9//76/f/++vz//fr9//76/f/9+/3/wLmq/66mk//Mxrv/oI1t//PHgv/JfBP/mIZk/724qP/9+/3//fr8//37/P/9+v3//fr9//36/P/9+v3//fr9//36/f/9+vz//fr8//36/f/9+vz//fr8/6uklP+Yjnj/wLms/352kf+Gguz/DAnE/4F4d//Y1Mv//vr9//36/P/9+v3//fr9//36/P/9+v3//fr9//36/P/9+v3//fr9//36/P/9+v3//fr9//36/P/9+v3//fr9//36/P/9+vz/1NDE/8XAs//SzML/noxs//PJgf/GfBP/modn/763qP/9+v3//fr8//36/P/++/3//vv9//77/f/++/3//vv9//77/P/++/3//vv9//77/P/++/3//fr8/+jl4v/f29b/zMe8/4B4kf+Mhuz/CwnC/4B4df/Y1Mv//vr9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//fr9//37/f/a1sz/n4xu//PIgf/DfhP/mYhm/764qP/++v3//vv9//77/f/9+v3//vv8//36/f/9+v3//vv9//77/f/++/3//fr8//77/f/++/3//vv8//77/f/9+/z/zcm+/4J4kv+PiO3/DAnC/4B4df/Y08v//vr9//77/f/++/3//fr9//77/f/++/3//fr9//77/f/++/3//fr9//77/f/++/3//fr9//77/f/++/3//fr9//77/f/++/3//fr8/722qP/JxLf/n4xu//PHgP/CfxP/mYhm/765qf/9+v3//fr8//77/f/9+vz//fr8//36/f/9+v3//fr9//36/P/9+v3//fr8//36/P/9+vz//fr9//37/P+dl4L/vbao/4J4k/+Piev/DArD/4B4df/X08v//fr9//36/f/9+vz//fr8//36/f/9+vz//fr8//36/f/9+vz//fr8//36/f/9+vz//fr8//36/f/9+vz//fr8//36/f/9+vz//Pv8/9HMw//QysD/notu//bKg//CfhL/modl/7+5qf/9+v3//fr8//36/f/++/3//vv9//77/f/++/3//vv9//77/f/++/z//vv9//77/f/++/3//vv9//77/P/u6+n/zMe9/4J4k/+Piuv/DArD/4B4df/X08v//vr9//77/P/++/z//vv9//77/P/++/z//vv9//77/P/++/z//vv9//77/P/++/z//vv9//77/P/++/z//vv9//77/P/++/z//fv9//36/f/a1c7/noxu//XJhP/EfhP/nIZl/724qP/++/3//vv9//77/f/++/3//vv9//36/P/9+vz//fr8//77/f/++/z//fr8//77/f/++/3//fr8//77/P/++/3/zcnA/4J4k/+Piev/DArE/4B4df/X08v//vr9//77/P/++/z//fr9//77/P/++/z//fr9//77/P/++/z//fr9//77/P/++/z//fr9//77/P/++/z//fr9//77/P/++/z//fr8/7y4qP/KxLf/n4xt//TIg//FfxP/nYVk/7y4p//++v3//fr9//76/P/9+vz//fr8//36/P/9+vz//fr9//36/P/9+vz//fr8//36/P/9+vz//fr8//37/P+YlX3/u7Wm/4J5kv+MiOz/DArE/4B4df/X08v//fr9//36/P/9+vz//fr8//36/P/9+vz//fr8//36/P/9+vz//fr8//36/P/9+vz//fr8//36/P/9+vz//fr8//36/P/9+vz//Pv8/9DLw//Qyr//oI5s/+/GgP/KgBP/m4hn/764qP/9+v3//fr8//36/P/++/3//vv8//77/P/++/3//vv8//77/P/++/z//vv8//77/P/++/3//vv9//77/P/18vH/zci8/4N4kv+Mhuz/DQnD/4B5df/X08v//vr9//77/P/++/z//vv8//77/P/++/z//vv8//77/P/++/z//vv8//77/P/++/z//vv8//77/P/++/z//vv8//77/P/++/z//vr9//36/f/b1c7/rKOO/+zavP/VrGP/vLWh/7+5qf/++v3//vv9//77/f/++/3//vv9//36/P/9+v3//vv8//77/P/++/z//fr9//77/P/++/3//fr8//77/P/++/3/z8m+/4N4kv+Nhuv/DQnD/394dP/X08v//vr9//37/P/9+/z//fr9//37/P/9+/z//fr9//37/P/9+/z//fr9//37/P/9+/z//fr9//37/P/9+/z//fr9//37/P/9+/z//Pv9/7y3p//Mxbj/rKaT//z6/f/6+vz/xcGx/765qf/++v3//fr8//77/f/9+v3//fr8//36/f/9+v3//fr8//36/P/9+vz//fr9//36/P/9+v3//fr9//37/P+UjXj/vbWm/4B3j/+QiOn/DwnE/4B5c//X08v//vr9//36/f/9+v3//fr8//36/f/9+v3//fr8//36/f/9+v3//fr8//36/f/9+v3//fr8//36/f/9+v3//fr8//36/f/9+v3//fv8/9DNwv/Ry7//qqWT//37/f/9+v3/xcCx/765qP/9+v3//fr8//36/P/++/z//vv9//77/f/++/z//vv9//77/P/++/z//vv9//77/P/++/3//vv9//77/f/79/f/z8m+/5iRlP+ZkOH/JSDC/5iQhf/X08r//vr9//77/P/++/z//vv9//77/P/++/z//vv9//77/P/++/z//vv9//77/P/++/z//vv9//77/P/++/z//vv9//77/P/++/z//fr9//z7/f/b1c7/q6aT//77/f/++/3/xcGx/765qP/++v3//vv9//77/f/9+v3//vv9//36/f/9+v3//vv8//77/P/++/z//fr8//77/P/++/3//fr9//77/f/++/3/z8q//7awnf/3+Pn/8vH3/66mlP/Y08v//vr9//37/f/++/3//fr9//37/f/++/3//fr9//37/f/++/3//fr9//37/f/++/3//fr9//37/f/++/3//fr9//37/f/++/3//Pv8/8C4qv/Lxbj/q6aT//77/f/++/z/xcGy/765qf/++v3//fr8//77/f/9+vz//fr9//36/f/9+vz//fr8//36/P/9+v3//fr8//36/P/9+vz//fr9//37/P+MiXD/u7Wl/7iyoP/9+v3//fv8/6+mlP/Y08v//vr9//36/f/9+vz//fr9//36/f/9+vz//fr9//36/f/9+vz//fr9//36/f/9+vz//fr9//36/f/9+vz//fr9//36/f/9+vz//fr8/9LNwv/RysD/qqWT//36/f/9+v3/xcCy/765qP/9+v3//fr8//36/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv8//37/P/8+/n/zsq+/7iyof/++v3//vv8/66llP/Y08v//vr9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//fv9//37/f/b1s7/qqaT//77/P/++/3/xcCy/765qP/++v3//vv9//77/P/9+vz//vv9//36/P/9+v3//vv9//77/f/++/z//vr9//77/f/9+vz//vv8//37/P/++/z/z8q+/7myov/9+v3//vv8/66lk//Y08v//vr9//77/P/++/3//fr8//77/P/++/3//fr8//77/P/++/3//fr8//77/P/++/3//fr8//77/P/++/3//fr8//77/P/9+vz/wbmr/6+mlv/Ox7z/q6aT//77/f/++/3/xcCy/766qP/++v3//fr9//77/f/9+v3//fr9//36/f/9+vz//fr9//36/f/9+v3//fr9//36/f/9+v3//fr8/5ePdv96cVL/vrio/7iyof/9+v3//fv8/66lk//Y08v//vr9//36/P/9+v3//fr9//36/P/9+v3//fr9//36/P/9+v3//fr9//36/P/9+v3//fr9//36/P/9+v3//fr9//36/P/9+vz/1dDG/8e/s//TzcL/qqWT//36/f/9+v3/xcCy/7+6qP/9+v3//fr9//36/f/++/3//vv8//77/P/++/3//vv8//77/P/++/z//vv9//77/P/++/z//fv8//z7/P/9+vr/zsq+/7iyof/++v3//vv8/66lk//Y08v//vr9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//Pv9//z6/f/c1s//qqWT//77/f/++/3/xcGy/7+6qP/++v3//vv8//77/f/9+vz//vv8//37/f/++v3//vr9//77/P/++/3//fr8//77/P/++/3//fr9//37/P/6+/n/zsq+/7iyof/++v3//vv8/6+mlP/Y08v//vr9//77/f/++/z//fr9//77/f/++/z//fr9//77/f/++/z//fr9//77/f/++/z//fr9//77/f/++/z//fr9//77/f/++/z/+/v8/723pv/Mxbn/q6aT//77/f/++/3/xcGy/7+6qf/++/3//fr8//77/f/9+vz//fr9//36/P/9+vz//fr8//36/f/9+vz//fr8//36/f/9+v3//fr8//77/P+Qim3/urSl/7iyof/9+v3//vv8/6+llP/Y08v//vr9//36/P/9+vz//fr8//36/P/9+vz//fr8//36/P/9+vz//fr8//36/P/9+vz//fr8//36/P/9+vz//fr8//36/P/9+vz//fr8/8/Mwf/Ry8D/q6aT//36/P/9+v3/xcGy/7+6qf/9+v3//fr8//36/P/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/z//vv8//77/f/++/z/z8q//7iyof/++v3//vv8/6+mlP/Y08v//vr9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//fv8//z7/f/b1s7/qqWT//77/f/++/3/xsGy/766qf/++/3//vv9//77/f/9+vz//vv9//36/f/9+v3//vv9//77/f/++/3//fr8//77/f/++/3//fr8//76/f/59/X/z8q+/7iyof/++v3//vv8/6+mlP/Y08v//fr9//77/f/9+vz//fr9//77/f/9+vz//fr9//77/f/9+vz//fr9//77/f/9+vz//fr9//77/f/9+vz//fr9//77/f/9+vz//Pv8/7+7rP/Mxrr/qqaT//77/f/++/3/xsGy/765qf/++/3//fr9//77/f/++/z//vv9//77/P/++/z//vv9//77/P/++/z//vv8//77/P/++/3//vv9//77/P+TjHf/vLan/7myof/++v3//vv8/6+mlP/Y08v//vr9//77/f/++/z//vv9//77/f/++/z//vv9//77/f/++/z//vv9//77/f/++/z//vv9//77/f/++/z//vv9//77/f/++/z//fr8/9HMwf/SysD/qqaT//77/f/++/3/xcGy/765qf/++/3//vv8//77/f/9+v3//fr8//36/f/9+v3//fr8//36/f/9+v3//fr8//36/f/9+v3//fr9//76/P/++v3/0MvA/7iyof/9+v3//vv8/6+llP/Y08v//vr9//36/f/9+v3//fr8//36/f/9+v3//fr8//36/f/9+v3//fr8//36/f/9+v3//fr8//36/f/9+v3//fr8//36/f/9+v3//fr9//37/f/b1s7/qqWT//36/f/9+v3/xcGy/765qf/9+v3//fr9//36/f/++v3//vv9//36/f/9+vz//vv9//77/f/++/3//vr9//77/f/++/3//fr9//76/f/18/H/z8q+/7iyof/++v3//vv8/6+llP/Y08v//fr9//36/P/++/3//vr9//36/P/++/3//vr9//36/P/++/3//vr9//36/P/++/3//vr9//36/P/++/3//vr9//36/P/++/3//fr9/763rf/Mxbr/qqaT//77/f/++/3/xsGy/765qf/++/3//fr9//77/f/++/3//vv8//77/P/++/z//vv8//77/f/++/3//vv8//77/f/++/3//vv8//37/P+VkXr/vLem/7iyof/++v3//vv8/6+llP/Y08v//fr9//77/f/++/z//vv8//77/f/++/z//vv8//77/f/++/z//vv8//77/f/++/z//vv8//77/f/++/z//vv8//77/f/++/z//fr8/9PNxv/Ry8D/q6aT//77/P/++/z/xcGy/765qP/++v3//vv9//77/P/9+v3//fr8//36/P/9+v3//fr8//36/P/9+vz//fr9//36/P/9+v3//fr9//37/P/++/z/z8u//7iyof/9+v3//vv8/6+mlP/Y08v//fr9//36/f/9+vz//fr9//36/f/9+vz//fr9//36/f/9+vz//fr9//36/f/9+vz//fr9//36/f/9+vz//fr9//36/f/9+vz//fv8//77/P/c1s3/q6aT//36/f/9+v3/xcGy/765qP/9+v3//fr8//36/f/9+vz//vv8//36/f/9+v3//vv9//76/P/++/3//fr9//76/P/++/3//vv9//36/f/v7Or/zci8/7iyof/++v3//vv8/6+mlP/Y08v//vr9//77/f/++/z//fr9//77/f/++/z//fr9//77/f/++/z//fr9//77/f/++/z//fr9//77/f/++/z//fr9//77/f/++/z//fv8/768rf/Lxrv/qqWT//77/f/++/3/xsGy/765qf/++/3//fr8//77/f/++/3//vv9//77/f/++/3//vv9//77/P/++/3//vv9//77/P/++/z//vv9//77/P+cloT/vLam/7iyof/++v3//fv9/6+mkv/Y08v//fr9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//fv8/8/Mwv/Ry8D/rKWS//77/P/++/3/xsGy/765qP/++/3//vv9//77/P/9+vz//fr8//36/P/9+vz//fr8//36/P/9+vz//fr8//36/P/9+vz//vr9//36/f/8+/z/zsq+/7iyof/++v3//fv8/6+mkv/Z1Mv//fv9//36/f/9+vz//fr9//36/f/9+vz//fr9//36/f/9+vz//fr9//36/f/9+vz//fr9//36/f/9+vz//fr9//36/f/9+vz//fv8//78/P/d183/rKWR//36/f/9+vz/xsGy/7+7qv/9+v3//fr8//36/f/++/3//vv9//36/P/9+v3//fr8//77/f/++/z//fr8//77/f/++/3//fr8/+fl4P/g2db/0c3A/6+olv/9+v3//fv8/6mgi//d2NH//vr9//77/P/++/3//fr9//77/P/++/3//fr9//77/P/++/3//fr9//77/P/++/3//fr9//77/P/++/3//fr9//77/P/9+vz/v7ut/6+nlP/W08f/nZN7//77/P/9+/3/tK6d/83Gu//++/3//fr8//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//fr8/62lkf+WjXT/5OHZ/350U//28/L/8vDu/4FxVf/59vX//vr9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/++/3//vv9//77/f/9+vz/0s7E/8a/sf/z8O7/fnVV/83Ivf/X08v/eW1Q//Xy8f/++/3//vv9//77/P/9+vz//fr9//36/f/9+vz//fr9//36/f/9+v3//fr9//36/f/9+vz//fr9//v6/v/9+vz//fr9/8XBtP9qXTz/bV89/83Huv/++/3//fr9//36/f/9+v3//fr9//36/f/9+v3//fr9//36/f/9+v3//fr9//36/f/9+v3//fr9//36/f/9+v3//fr9//36/f/9+v3//fr9//36/f/++/3/6Ofi/46EZ/+IfV//3tnT//37/f/9+v3//fr8//36/f8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='
with open('12.ico', 'wb') as tmp:
    tmp.write(base64.b64decode(Icon().img))
window.iconbitmap('12.ico')
os.remove('12.ico')

#菜单
menu1=Menu(window)
file=Menu(menu1,tearoff=0)
menu1.add_cascade(label='文件',menu=file),\
file.add_command(label='打开'),file.add_command(label='新建'),\
file.add_command(label='保存')
window.config(menu=menu1)

#面板
#pw = PanedWindow(window,orient='vertical',sashrelief='sunken')
#pw.pack(fill='both',expand=1)
  #状态栏
separator=ttk.Separator(window).pack(fill='x',padx=5)
status_frame=ttk.Frame(window,relief='raised').pack(fill='x')
label_status=ttk.Label(window,text=' ').pack(side='left',fill='x')
  #尺寸手柄
sizegrip=ttk.Sizegrip(status_frame).pack(anchor='ne')
#面板
#pw1 = PanedWindow(pw,orient='horizontal',sashrelief='sunken')
#pw2 = PanedWindow(pw,orient='horizontal',sashrelief='sunken')
#left_frame,right_frame, bottom_frame = Frame(pw1,width=140,relief='flat'),\
                                       #Frame(pw1,height=80,relief='flat'),\
                                       #Frame(pw2,relief='flat')
#pw.add(pw1),pw.add(pw2),pw1.add(left_frame),pw1.add(right_frame),pw2.add(bottom_frame)

#选项框
button,label,entry,radiobutton,checkbutton=ttk.Button(text='按钮'),\
    ttk.Label(text='标签'),ttk.Entry(),\
    ttk.Radiobutton(text='选项按钮'),ttk.Checkbutton(text='复选框')

button.place(relx=0.10,rely=0.54,width=70,height=40,anchor=CENTER)
label,entry.place(relx=0.10,rely=0.64,width=70,height=40,anchor=CENTER)
radiobutton.place(relx=0.10,rely=0.74,width=70,height=40,anchor=CENTER)
checkbutton.place(relx=0.10,rely=0.84,width=70,height=40,anchor=CENTER)

#进度条    选值框
labeledscale,spionbox=ttk.LabeledScale(from_=0,to=30,),\
                            ttk.Spinbox(from_=0,to=20,increment=2)
spionbox.place(relx=0.10,rely=0.37,width=80,height=23,anchor=CENTER)
labeledscale.place(relx=0.10,rely=0.44,width=70,height=40,anchor=CENTER)




#文本
k1=StringVar()

label1=Label(window,text="",font=("Comic Sans MS",12))
label2=Label(window,text="",font=("Comic Sans MS",12))

#输入框
number_entry1=Entry(window,textvariable=IntVar())

#输出框
e3 = Entry(window,textvariable=k1, state='readonly').place(relx=0.1,rely=0.2,anchor=CENTER)

#函数
def calculator():

    number1=number_entry1.get()
    number=float(number1)

    F = (number * 2)
    F=int(F)

    result =F
    k1.set(F)

#按键
press=Button(window,text="执行",font=("Comic Sans MS",12),command=calculator)

#布局
label1.place(relx=0.22,rely=0.50,anchor=CENTER)
label2.place(relx=0.22,rely=0.15,anchor=CENTER)
number_entry1.place(relx=0.1,rely=0.1,anchor=CENTER)
press.place(relx=0.1,rely=0.3,anchor=CENTER)

#保持
window.mainloop()