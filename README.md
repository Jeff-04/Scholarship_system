# Scholarship Selection System using SVM & SMART
this project is a system that was built to overcome the tendency of errors in awarding scholarships, there are lots of cases related to this problem such as:
1. https://voicesikka.com/2022/07/17/beasiswa-salah-sasaran-area-rugi-rp-280-juta-jaksa-harus-periksa-kabag-kesra/
2. https://www.kompas.com/tren/read/2023/02/10/131500765/kip-kuliah-disebut-salah-sasaran-karena-penerimanya-nonton-konser-dan-beli?page=all
3. https://rakyatbengkulu.disway.id/read/645736/beasiswa-bpdpks-disepsi-salah-sasaran
   
This project uses 2 stages of selection, the first is using a support vector machine algorithm and the second is using a simple multi attribute rating technique expert system.

# Algorithm
## Support Vector Machine
<img src="Images/svm.jpg" alt="Support Vector Machine" style="width: 75%;">
Support Vector Machine (SVM) is one of the algorithms machine learning that is used to perform classification and regression.
The basic concept of a support vector machine (SVM), viz build a fruit hyperplane (separator) between the data with maximize the distance in each existing category.

The data used in the support vector machine is of type text data which has 4 columns:
1. Kartu Indonesia Pintar (KIP)
   has 2 types of value categories, namely yes and no
2. Penghasilan Orang Tua
   has 3 types of value categories, namely below 1 million, above 1 million and no income
3. Status Orang Tua Siswa
   has 3 types of categories namely complete, fatherless / motherless, orphan
4. Data Kemiskinan Dinas Sosial
   has 3 types of categories namely poor, vulnerable poor and normal
5. Target
   has 2 types of categories (yes / no)

Complete data can be seen [here](./dataset/data_final.csv)

In the process of creating a support vector machine model, I didn't use a library because the data has less complex values, so I decided to make manual svm calculations. The principle used is as shown in the following figure:<br>
<html>
<head>
   <style>
      #page {
         border-collapse: collapse;
      }
   
      #page td {
         padding: 0; 
         margin: 0;
      }
   </style>
</head>
<table id="page">
  <tr>
      <td rowspan="2"><img src="Images/support vector machine.png" alt="svm concept" style="width: 100%;"></td>
      <td><img src="Images/rumus-1.png" alt="formula-1" style="width: 75%;"></td
  </tr>
  <tr>
      <td><img src="Images/rumus-2.png" alt="formula-1" style="width: 75%;"></td
  </tr>
</table>
</html>

## Simple Multi Attribute Rating Technique


Live Demo : https://jeff-04-seminar-tematik-beasiswa-main-hno1py.streamlit.app/
