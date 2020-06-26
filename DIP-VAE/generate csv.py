import os
import pandas as pd
# image,MEL,NV,BCC,AKIEC,BKL,DF,VASC
BASE_DIR = "/home/madnerd/PycharmProjects/DataScience/Dataset_skin_cancer/akiec/"

images = []
labels1 = []
labels2 = []
labels3 = []
labels4 = []
labels5 = []
labels6 = []
labels7 = []
labels8 = []
labels9 = []

label1_akiec = 1.0
label2_bcc = 0.0
label3_bkl = 0.0
label4_df = 0.0
label5_mel = 0.0
label6_nv = 0.0
label7_nv2 = 0.0
label8_nv3 = 0.0
label_9_vasc = 0.0

for root, dirs, files in os.walk(BASE_DIR, topdown=False):
    for name in files:
        string = name
        images.append(string)
        labels1.append(label1_akiec)
        labels2.append(label2_bcc)
        labels3.append(label3_bkl)
        labels4.append(label4_df)
        labels5.append(label5_mel)
        labels6.append(label6_nv)
        labels7.append(label7_nv2)
        labels8.append(label8_nv3)
        labels9.append(label_9_vasc)

df = pd.DataFrame()
df['images'] = images
df['akiec'] = labels1
df['bcc'] = labels2
df['bkl'] = labels3
df['df'] = labels4
df['mel'] = labels5
df['nv'] = labels6
df['nv2'] = labels7
df['nv3'] = labels8
df['vasc'] = labels9


df.to_csv('akiec.csv', header=None)
