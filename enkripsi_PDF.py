from PyPDF2 import PdfWriter, PdfReader 
  
# buat objek pdf writer
out = PdfWriter()
  
# buka file pdf asli 
file = PdfReader("E:/UNS/MATA KULIAH/Sistem Keamanan Data/Materi_Praktikum/RSA/file_pdf.pdf")
  
# identifikasi total halaman file
num = len(file.pages)
  
#program membaca setiap halaman file sesuai halaman yg diidentifikasi 
for idx in range(num):
    
    page = file.pages[idx]
      

    out.add_page(page)
  
  
# masukkan password enkripsi 
password = "pass"
  
# enkripsi masing-masing halaman 
out.encrypt(password)
  
# buka file enkripsi "myfile_encrypted.pdf"
with open("E:/UNS/MATA KULIAH/Sistem Keamanan Data/Materi_Praktikum/RSA/myfile_encrypted.pdf", "wb") as f:
    
    # simpan pdf 
    out.write(f)
