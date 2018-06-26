import os

def pdf2jpg(pdf_path):
    os.system('tool\\mutool.exe draw -o PIC_OUT\\out%d.png '+ pdf_path)


if __name__ == '__main__':
    pdf_path = 'PDF_FILE_NAME/1.pdf'
    pdf2jpg(pdf_path)

