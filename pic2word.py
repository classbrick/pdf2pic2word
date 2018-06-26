from aip import AipOcr
import json

""" 你的 APPID AK SK """
APP_ID = '11443085'
API_KEY = 'F0YPpEqVtRGFhsGMgFlYCqCG'
SECRET_KEY = 'tDd2rMcLbencXwpS7be6BCZsfzFLLNan'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def pic2word(pic_path):
    image = get_file_content(pic_path)

    """ 调用通用文字识别, 图片参数为本地图片 """
    client.basicGeneral(image)

    """ 如果有可选参数 """
    options = {}
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    options["probability"] = "true"

    """ 带参数调用通用文字识别, 图片参数为本地图片 """
    baidu_ret = client.basicGeneral(image, options)
    return get_word(baidu_ret)

def url2word(url = "https//www.x.com/sample.jpg"):
    """ 调用通用文字识别, 图片参数为远程url图片 """
    client.basicGeneralUrl(url)

    """ 如果有可选参数 """
    options = {}
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    options["probability"] = "true"

    """ 带参数调用通用文字识别, 图片参数为远程url图片 """
    return client.basicGeneralUrl(url, options)


def get_word(baidu_ret):
    ret = ''
    for i in baidu_ret['words_result']:
        ret += i['words'] + '\n'
    return ret


if __name__ == '__main__':
    pic_path = 'D:/Users/zhengnan.luo/PycharmProjects/pdf2png2word/pdf2png2word/PIC_OUT/out1.png'
    baidu_ret = pic2word(pic_path)



