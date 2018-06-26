import pdf2png
import pic2word
import os
import shutil

pdf_path = 'PDF_FILE_NAME/1.pdf'
tool_path= 'tool\\mutool.exe'
pic_path = 'PIC_OUT/'
word_path = 'WORD_OUT/'


def pdf2word(pdf_path, pic_path, word_path):
    os.system('echo \"delete the past pictures\"')
    if os.path.exists(pic_path):
        shutil.rmtree(pic_path)
        os.makedirs(pic_path)
    os.system('echo \"delete the past texts\"')
    if os.path.exists(word_path):
        shutil.rmtree(word_path)
        os.makedirs(word_path)
    pdf2png.pdf2jpg(pdf_path)
    os.system('echo \"start to convert the pictures\"')
    for root, dirnames, filenames in os.walk(pic_path):
        for file in filenames:
            os.system('echo converting %s' % file)
            word_path_temp = os.path.join(word_path, os.path.basename(file) + '.txt')
            file = os.path.join(root, file)
            word = pic2word.pic2word(file)
            with open(word_path_temp, 'w') as fileobject:  # 使用‘w’来提醒python用写入的方式打开
                fileobject.write(word)


if __name__ == '__main__':
    pdf2word(pdf_path, pic_path, word_path)
    os.system(
        'echo \"all pictures are converted, dont forget to rest when work overtime, lai wan wang zhe rong yao ba!~\"')
    os.system('pause')

