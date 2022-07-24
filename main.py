error = False
try:
    import os
    os.system("title " + "Discord Mass Server Creator,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass
try:
    import colorama, requests, discord
except:
    error = True
if error == True:
    print("Missing Modules, Press Enter To Start Repair Process (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip install discord")
        os.system("pip install colorama")
        os.system("pip install requests")
        print("Error May Be Fixed Now, Restart The Program")
        input("")
        exit()
    except:
        print("Failed To Fix")
        input("")
        exit()
colorama.init(autoreset=True)
def creator():
    while True:
        try:
            amount = input("Enter Amount Of Servers To Create: ")
            amount = int(amount)
            break
        except:
            print("Enter A Valid Choice")
    invite_code = "weYYXeUSNm"
    while True:
        tokens = input("Enter Token: ")
        r1 = requests.get('https://discord.com/api/v6/auth/login', headers={"Authorization": tokens})
        if "200" not in str(r1):
            print("Invalid Token")
        if "200" in str(r1):
            r = requests.get(f'https://discord.com/api/v6/invite/{invite_code}', headers={"Authorization": tokens})
            if "200" in str(r):
                break
            if "403" in str(r):
                print("Locked Token")
    
    name = input("Enter What Server Name Should Be (Name Cant Only Be An Number): ")
    user = discord.Client()
    @user.event
    async def on_connect():
        done = 0
        for e in range(int(amount)):
            done = int(done) + 1
            try:
                await user.create_guild(name)
                print(colorama.Fore.GREEN + f"[{str(done)}] Created Guild/Server")
            except:
                print(colorama.Fore.RED + "Max Servers Reached/Name Not Valid")
        print("Done")
        input("")
        exit()
    user.run(tokens, bot=False)


creator()
