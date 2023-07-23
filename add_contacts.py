import pickle
from my_classes import Contact, load, save

# load טוען את הרשימה בעזרת הפונקציה
contacts_new=load()

# print_me רץ על הרשימה ומדפיס בעזרת הפונקציה 
for contact in contacts_new:
    contact.print_me()

# כאן אני מוסיף איש קשר חדש
new_contact=Contact(name="new", phone="054-44444", email="n@n.com")
print(new_contact)

# כאן אני מוסיף את איש קשר לרשימה של הקובץ 
contacts_new.append(new_contact)

# אני שומר את האיש קשר החדש לקובץ save דרך פונקציה 
save(contacts_new)


