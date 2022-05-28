import telegram
from telegram import *
from telegram.ext import *
import S5Crypto
import socket
import time
import os
from JDatabase import JsonDatabase
import start

permitidos = ["AresDza","diago8888","Guachineo","FriendXfriendss","manzanatg","Juanedu_10"]

def filtrar_text(update, context):
    text = update.message.text
    username = update.effective_user.username
    if (username == administrador and administrador in permitidos) or (username in permitidos and administrador in permitidos):
        try :
            jdb = JsonDatabase('database')
            jdb.check_create()
            jdb.load()

            user_info = jdb.get_user(username)

            if username == administrador or user_info :  # Validar Usuario
                if user_info is None:
                    if username == administrador:
                        jdb.propietario(username)
                    else:
                        jdb.propietario(username)
                    user_info = jdb.get_user(username)
                    jdb.save()
            else:return
        except:pass

        if '/start' in text:
            getUser = user_info
            if getUser:
                statInfo = start.start_i(username,getUser,jdb.is_admin(username))
                bot.sendMessage(update.message.chat.id,statInfo)
                return

        if '/getdb' in text:
            isadmin = jdb.is_admin(username)
            if isadmin:
                bot.sendMessage(update.message.chat.id,'🔷BASE DE DATOS🔷\n🔹NO COMPARTIR🔹')
                with open("database.jdb", "rb") as db:
                    bot.sendDocument(chat_id=update.message.chat.id, parse_mode="HTML", document=db)
            else:
                    bot.sendMessage(update.message.chat.id,'✖️No Tiene Permiso✖️')
            return

        if '/pr_find' in text:
            try:
                try:
                    try:id_msg = int(update.message.message_id) + 1
                    except Exception as ex:bot.sendMessage(update.message.chat.id,ex)
                    rango_min = str(str(text).split('-')[0]).split(' ')[1]
                    rango_max = str(str(text).split('-')[1]).split(' ')[0]
                    ip = str(text).split(' ')[2]
                    msg_start = '🛰 Buscando Proxy en el Rango de Puerto : '+rango_min+' - '+rango_max+'\nIP : '+ip+'!!\n\n⏳ Por favor espere .....'
                    print("Buscando proxy...")
                    try:
                        getUser = user_info
                        if getUser:
                            getUser['rango_minimo'] = rango_min
                            getUser['rango_maximo'] = rango_max
                            getUser['ip'] = ip
                            jdb.save_data_user(username,getUser)
                            jdb.save()
                    except:
                        bot.sendMessage(update.message.chat.id,'✖️Error al Guardar IP y Rango de Puertos✖️')
                    bot.sendMessage(update.message.chat.id,msg_start)
                    time.sleep(1.5)
                    try:bot.editMessageText(chat_id=update.message.chat.id,message_id=id_msg,text=f"{msg_start}\n\n➖➖➖➖➖➖➖\nBuscando proxy...\n\n➖➖➖➖➖➖➖")
                    except Exception as ex:bot.sendMessage(update.message.chat.id,ex)
                    for port in range(int(rango_min),int(rango_max)):
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        result = sock.connect_ex((ip,port))

                        if result == 0:
                            pr_find=1
                            print ("Puerto abierto!")
                            print (f"Puerto: {port}")
                            try:bot.editMessageText(chat_id=update.message.chat.id,message_id=id_msg,text=f"{msg_start}\n\n➖➖➖➖➖➖➖\nPuerto abierto!\nPuerto: {port}\n➖➖➖➖➖➖➖")
                            except Exception as ex:bot.sendMessage(update.message.chat.id,ex)
                            proxy = f'{ip}:{port}'
                            proxy_new = S5Crypto.encrypt(f'{proxy}')
                            time.sleep(5)
                            msg = 'Su nuevo proxy es:\n\nsocks5://' + proxy_new
                            try:bot.editMessageText(chat_id=update.message.chat.id,message_id=id_msg,text=f"{msg}")
                            except Exception as ex:bot.sendMessage(update.message.chat.id,ex)
                            break
                        else:
                            pr_find=0
                            print ("Error...Buscando...")
                            print (f"Buscando en el puerto: {str(port)}")
                            sock.close()
                            try:bot.editMessageText(chat_id=update.message.chat.id,message_id=id_msg,text=f"{msg_start}\n\n➖➖➖➖➖➖➖\nError...Buscando...\nBuscando en el Puerto: {str(port)}\n➖➖➖➖➖➖➖")
                            except Exception as ex:bot.sendMessage(update.message.chat.id,ex)
                    try:
                        if pr_find==0:
                            bot.editMessageText(chat_id=update.message.chat.id,message_id=id_msg,text=f"🛰 No Hubo Éxito Buscando Proxy!!\n\n❌ IP : {ip}\n\n❌ PUERTOS : {rango_min}-{rango_max}")
                        else:pass
                    except Exception as ex:print(str(ex))
                    return
                except:
                    try:
                        getUser = user_info
                        if getUser:
                            ip = getUser['ip']
                            rango_min = getUser['rango_minimo']
                            rango_max = getUser['rango_maximo']
                    except:
                        rango_min = "2080"
                        rango_max = "2085"
                        ip = "181.225.253.188"
                    try:id_msg = int(update.message.message_id) + 1
                    except Exception as ex:bot.sendMessage(update.message.chat.id,ex)
                    msg_start = '🛰 Buscando Proxy!!\n\n⏳ Por favor espere .....'
                    print("Buscando proxy...")
                    bot.sendMessage(update.message.chat.id,msg_start)
                    time.sleep(1.5)
                    try:bot.editMessageText(chat_id=update.message.chat.id,message_id=id_msg,text=f"{msg_start}\n\n➖➖➖➖➖➖➖\nBuscando proxy...\n\n➖➖➖➖➖➖➖")
                    except Exception as ex:bot.sendMessage(update.message.chat.id,ex)
                    for port in range(int(rango_min),int(rango_max)):
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        result = sock.connect_ex((str(ip),port))

                        if result == 0:
                            pr_find=1
                            print ("Puerto abierto!")
                            print (f"Puerto: {port}")
                            try:bot.editMessageText(chat_id=update.message.chat.id,message_id=id_msg,text=f"{msg_start}\n\n➖➖➖➖➖➖➖\nPuerto abierto!\nPuerto: {port}\n➖➖➖➖➖➖➖")
                            except Exception as ex:bot.sendMessage(update.message.chat.id,ex)
                            proxy = f'{ip}:{port}'
                            proxy_new = S5Crypto.encrypt(f'{proxy}')
                            time.sleep(5)
                            msg = 'Su nuevo proxy es:\n\nsocks5://' + proxy_new
                            try:bot.editMessageText(chat_id=update.message.chat.id,message_id=id_msg,text=f"{msg}")
                            except Exception as ex:bot.sendMessage(update.message.chat.id,ex)
                            break
                        else:
                            pr_find=0
                            print ("Error...Buscando...")
                            print (f"Buscando en el puerto: {port}")
                            sock.close()
                            try:bot.editMessageText(chat_id=update.message.chat.id,message_id=id_msg,text=f"{msg_start}\n\n➖➖➖➖➖➖➖\nError...Buscando...\nBuscando en el Puerto: {port}\n➖➖➖➖➖➖➖")
                            except Exception as ex:print(str(ex))
                    try:
                        if pr_find==0:
                            bot.editMessageText(chat_id=update.message.chat.id,message_id=id_msg,text=f"🛰 No Hubo Éxito Buscando Proxy!!\n\n❌ IP : {ip}\n\n❌ PUERTOS : {rango_min}-{rango_max}")
                        else:pass
                    except Exception as ex:print(str(ex))
                    return
            except: bot.sendMessage(update.message.chat.id,"ERROR")
        if '/add_user' in text:
            isadmin = jdb.is_admin(username)
            if isadmin:
                try:
                    user = str(text).split(' ')[1]
                    jdb.create_user(user)
                    jdb.save()
                    msg = '👤 @'+user+' ahora Tiene Acceso al BOT como [USUARIO]'
                    bot.sendMessage(update.message.chat.id,msg)
                except:
                    bot.sendMessage(update.message.chat.id,'✖️Error en el comando /add_user username✖️')
            else:
                bot.sendMessage(update.message.chat.id,'✖️No Tiene Permiso✖️')
            return
        if '/kick_user' in text:
            isadmin = jdb.is_admin(username)
            if isadmin:
                try:
                    user = str(text).split(' ')[1]
                    if user == username:
                        bot.sendMessage(update.message.chat.id,'✖️No Se Puede Banear Usted✖️')
                        return
                    jdb.remove(user)
                    jdb.save()
                    msg = '🚪 @'+user+' ha sido Expulsado 👋🏻'
                    bot.sendMessage(update.message.chat.id,msg)
                except:
                    bot.sendMessage(update.message.chat.id,'✖️Error en el comando /kick_user username✖️')
            else:
                bot.sendMessage(update.message.chat.id,'✖️No Tiene Permiso✖️')
            return

    else :
        update.message.reply_text(text="@"+username+" no tienes acceso al bot")

# TOKEN
if __name__ == '__main__':
    administrador = os.environ.get('administrador')
    bot_token = os.environ.get('bot_token')
    bot = telegram.Bot(token=bot_token)
    updater = Updater(token=bot_token, use_context=True)

# Despachadores
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.text, callback=filtrar_text))

# Para Ejecutar el Bot
    updater.start_polling()
    print("Ejecutando el bot @" + bot.username)
    updater.idle()
