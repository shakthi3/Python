Login = lambda loginid, name, password: "Login Successfully" if (
    loginid == "User333"
    and name == "Meena"
    and password == "333"
) else "Login Failed"

print(Login("User333", "Meena", "333"))
