import os
import numpy as np
import pandas as pd
import nibabel as nib
import scipy.io as sio
from radiomics import featureextractor

def featureextract(main_path):
    main_dir = os.listdir(main_path)
    total_num = len(main_dir)
    param_path = 'exampleCT_2mm_label1.yaml'
    extractor = featureextractor.RadiomicsFeatureExtractor(param_path)
    df = pd.DataFrame()

    for i in range(total_num):
        patient_path = os.path.join(main_path, main_dir[i])
        print(patient_path)
        img_path = os.path.join(patient_path, 'imgCV.nii.gz')
        mask_path = os.path.join(patient_path, 'maskCV.nii.gz')

        featureVector = extractor.execute(imageFilepath=img_path, maskFilepath=mask_path)
        df_add = pd.DataFrame.from_dict(featureVector.values()).T
        df_add.columns = featureVector.keys()
        df = pd.concat([df, df_add])
    df.to_excel('RadiomicsFeature_CV.xlsx')


def getpatientname(main_path):
    main_dir = os.listdir(main_path)
    total_num = len(main_dir)
    df = pd.DataFrame()

    for i in range(total_num):
        patient_path = os.path.join(main_path, main_dir[i])
        print(patient_path)

        namelist = []
        namelist.append(main_dir[i])
        df_name = pd.DataFrame(data=namelist, columns=['patientname'])
        df = pd.concat([df, df_name])
        df.to_excel('patientname_CV.xlsx')

def main():
    main_path = 'I:\\Data\\Data_Mat_proc'
    featureextract(main_path)
    getpatientname(main_path)

if __name__ == "__main__":
    main()





