"""
Principio Open/Closed (OCP)
----------------------------
Este principio establece que las clases deben estar abiertas a la extensión (puedes agregar nuevas funcionalidades),
pero cerradas a la modificación (no debes cambiar el código existente).
"""

# VERSIÓN INCORRECTA cada vez que queramos añadir un nuevo tipo de notificación tenemos que modificar la clase
class Notificadon_malo:
    def enviar_notificacion(self, tipo, mensaje):
        if tipo == "email":
            return f"Enviando email: {mensaje}"
        elif tipo == "sms":
            return f"Enviando SMS: {mensaje}"
        elif tipo == "push":
            return f"Enviando notificación push: {mensaje}"

#VERSIÓN CORRECTA
class Notificacion:
    def enviar(self,mensaje):
        pass   

class NotificacionEmail(Notificacion):
    def enviar(self, mensaje):
        return f"Enviando email: {mensaje}"

class NotificacionSMS(Notificacion):
    def enviar(self, mensaje):
        return f"Enviando SMS: {mensaje}"

class NotificacionPush(Notificacion):
    def enviar(self, mensaje):
        return f"Enviando notificación push: {mensaje}"    
    
     
    
if __name__ == "__main__":   
    email = NotificacionEmail()
    print(email.enviar("Tienes un nuevo mensaje por email."))

    sms = NotificacionSMS()
    print(sms.enviar("Tienes un nuevo mensaje por SMS."))

    push = NotificacionPush()
    print(push.enviar("Tienes un nuevo mensaje por notificación push."))