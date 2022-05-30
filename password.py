password = "ThisisYourPassword2!"
enter_password = ""
password_try_count = 0
password_try_limit = 3
out_of_attempt = False

while enter_password != password and not(out_of_attempt):
    if password_try_count < password_try_limit:
        enter_password = input("Enter your password here (case sensitive): ")
        password_try_count += 1
    else:
        out_of_attempt = True
if out_of_attempt:
    print("Login failure. Try again after 1 hour.")
else:
    print("Logging in. Welcome back!")




