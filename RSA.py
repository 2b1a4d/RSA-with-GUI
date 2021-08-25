#导入相关库
import base64
import rsa
import tkinter
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
#设定密钥长度
def get_key_length():
    global key_length
    key_length = input_key_length.get()
    key_length = int(key_length)
#依据设定的密钥长度生成一对密钥
def generate_key():
    global key_length
    public_key,private_key = rsa.newkeys(key_length)
    #保存公钥与私钥
    public_key = public_key.save_pkcs1()
    file_public_key = open(asksaveasfilename(title = '保存公钥')+'.txt','wb')
    file_public_key.write(public_key)
    private_key = private_key.save_pkcs1()
    file_private_key = open(asksaveasfilename(title = '保存私钥')+'.txt','wb')
    file_private_key.write(private_key)
    #关文件
    file_public_key.close()
    file_private_key.close()
#导入公钥
def get_public_key():
    global public_key
    file_public_key = open(askopenfilename(),"rb")
    file_public_key = file_public_key.read()
    public_key = rsa.PublicKey.load_pkcs1(file_public_key)
#导入私钥
def get_private_key():
    global private_key
    file_private_key = open(askopenfilename(),"rb")
    file_private_key = file_private_key.read()
    private_key = rsa.PrivateKey.load_pkcs1(file_private_key)
#用公钥加密
def encrypt():
    global public_key
    #导入明文框文本编码为UTF-8并用已导入的公钥加密为密文
    plain_text = io_plain_text.get(index1=0.0,index2="end")
    plain_text = rsa.encrypt(plain_text.encode("UTF-8"),public_key)
    #密文字节用base64编码并输出至密文框
    plain_text = base64.b64encode(plain_text)
    plain_text = plain_text.decode("UTF-8")
    io_cipher_text.insert(0.0,plain_text)
#用私钥解密
def decrypt():
    global private_key
    #导入密文框base64编码并解码为原密文的字节
    cipher_text = io_cipher_text.get(index1=0.0,index2="end")
    cipher_text = base64.b64decode(cipher_text)
    #密文用已导入的私钥解密并编码为UTF-8并输出至明文框
    cipher_text = rsa.decrypt(cipher_text,private_key)
    cipher_text = cipher_text.decode("UTF-8")
    io_plain_text.insert(0.0,cipher_text)
#清空明文框
def delete_plain_text():
    io_plain_text.delete(index1=0.0,index2="end")
#清空密文框
def delete_cipher_text():
    io_cipher_text.delete(index1=0.0, index2="end")
#GUI界面
window = tkinter.Tk()
window.title('PC端简易RSA')
window.minsize(600,400)
#密钥相关操作
input_key_length = tkinter.Spinbox(window,values = ('未选择','1024','2048','4096'),command = get_key_length)
input_key_length.place(x=50,y=25)
output_key = tkinter.Button(window,text = "生成一对密钥",width = 12,height = 1,command = generate_key)
output_key.place(x=225,y=20)
input_public_key = tkinter.Button(window,text = "导入公钥",width = 12,height = 1,command = get_public_key)
input_public_key.place(x=325,y=20)
input_private_key = tkinter.Button(window,text = "导入私钥",width = 12,height = 1,command = get_private_key)
input_private_key.place(x=425,y=20)
#明文框部分
io_plain_text = tkinter.Text(window,width = 60,height = 6)
io_plain_text.place(x=120,y=80)
use_public_key = tkinter.Button(window,text = "用公钥加密",width = 10,height = 2,command = encrypt)
use_public_key.place(x=25,y=80)
clear_plain_text = tkinter.Button(window,text = "清空明文框",width = 10,height = 2,command = delete_plain_text)
clear_plain_text.place(x=25,y=130)
#密文框部分
io_cipher_text = tkinter.Text(window,width = 60,height = 6)
io_cipher_text.place(x=120,y=250)
use_private_key = tkinter.Button(window,text = "用私钥解密",width = 10,height = 2,command = decrypt)
use_private_key.place(x=25,y=250)
clear_cipher_text = tkinter.Button(window,text = "清空密文框",width = 10,height = 2,command = delete_cipher_text)
clear_cipher_text.place(x=25,y=300)

window.mainloop()