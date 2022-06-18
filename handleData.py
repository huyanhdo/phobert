import numpy as np
import re

dict = [['hsd','hạn sử dụng'],["ship", "vận chuyển"],["shop", "cửa hàng"],["m", "mình"],["mik","mình"],["ko","không"],['sz','size'],['rv','review'],['lm','làm'],['vsinh','vệ sinh'],
["k","không"],["kh","không"],["khong","không"],["kg","không"],["khg","không"],["tl","trả lời"],['zời','vời'],['ạh','ạ'],['zay','vậy'],['kb','không biết'],
["rep","trả lời"],["r","rồi"],["fb","facebook"],["face","faceook"],["thanks","cảm ơn"],["thank","cảm ơn"],['zậy','vậy'],['hy','hi'],['hog','không'],
["tks","cảm ơn"],["tk","cảm ơn"],["ok","tốt"],["oki","tốt"],["okie","tốt"],["sp","sản phẩm"],['ms','mới'],['ktra','kiểm tra'],['lém','lắm'],['hông','không'],
["dc","được"],["vs","với"],["đt","điện thoại"],["thjk","thích"],["thik","thích"],["qá","quá"],['wa','quá'],['trl','trả lời'],['bâyh','bây giờ'],
["trể","trễ"],["bgjo","bao giờ"],["h","giờ"],["qa","quá"],["dep","đẹp"],["xau","xấu"],["ib","nhắn tin"],['j','gì'],['hjc','hic'],['ltinh','linh tinh'],
["cute","dễ thương"],["sz","size"],["good","tốt"],["god","tốt"],["bt","bình thường"],["mn", "mọi người"], ['cb','chuẩn bị'],['phèng','phèn'],
["mng", "mọi người"], ["cx", "cũng"], ["bth", "bình thường"], ["flashsale", "sale"], ["ncl", "nói chung"],['nc','nói chung'],['nchung','nói chung'],
["mjnk", "mình"], ["ths", "cảm ơn"], ["r", "rồi"], ["oce" , "tốt"] , ["nma", "nhưng mà"], ["j", "gì"],['nhưg','nhưng'],['nhma','nhưng mà'],['nmà','nhưng mà'],
["lm", "làm"] , ["trc", "trước"], ["nh", "nhưng"] ,["dk", "được"], ["ng", "người"], ["mk", "mình"], ["ak", "à"],['àk','à'],['nhmà','nhưng mà'],
["bthg", "bình thường"], ["đc", "được"],["vid", "video"],["vx", "vẫn"],['chx', 'chưa'],['+','với'],['nhìu','nhiều'],['ctay','chia tay'],['kh','không'],
['t','tôi'],['đb','đầu buồi'],['ntin','nhắn tin'],['onl','online'],['nt','nhắn tin'],['vãi chưởng','vc'],['ji','gì'],['vd','ví dụ'],['tl','trả lời'],['ae','anh em'],
['nnao','như nào'],['bửn','bẩn'],['okay','ok'],['lsao','làm sao'],['wa','quá'],['lg','lượng'],['tôt','tốt']]

text = str("as'haha'đ")

def PreProcessing (text) :
    text1 = re.sub(r'([A-Z])\1+', lambda m: m.group(1).upper(), text, flags=re.IGNORECASE)
    text1 = re.sub(r'([),()])\1+', lambda m: m.group(1).upper(), text1, flags=re.IGNORECASE)
    text1 = text1.lower()
    text1 = re.sub("\n", " ", text1)
    text1 = re.sub(r"([?.!,¿])", " ", text1)
    text1 = re.sub(r'[" "]+', " ", text1)
    
    list_text = text1.split(" ")
    remover = []
    for chars in list_text :
        if len(chars) > 7 :
            remover.append(chars)
    for chars in remover :
        list_text.remove(chars)
    for i in range(len(list_text)):
        for j in range(len(dict)) :
            if (list_text[i] == dict[j][0]):
                list_text[i] = dict[j][1]
    text2 = " ".join(list_text)
    return text2
    
print("Câu ban đầu : " ,text)
print("Sau khi xử lí : ",PreProcessing(text))