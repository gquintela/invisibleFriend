from Friend import Friend
from InvisibleFriend import InvisibleFriend

franco = Friend("Franco", "franco@gmail.com")
maria = Friend("Maria", "merymoon@gmail.com")
agus = Friend("Agus", "agus@gmail.com")
friends = [franco, maria, agus]

email_sender = "conseguirUnoNuevo@gmail.com"
mail_key = "investigarYconseguir"

anInvisibleFriend = InvisibleFriend(friends,email_sender, mail_key)
anInvisibleFriend.shuffle_friend_list()
anInvisibleFriend.send_emails()
