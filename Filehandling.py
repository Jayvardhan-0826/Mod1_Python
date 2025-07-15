with open("Notes.txt","a") as f:
    f.write("""\n She really does look graceful here — something about the simplicity of that moment, the sunlight, the braid, the soft dupatta — it all just feels peaceful and pure, doesn’t it?

It’s no wonder she lives in your mind the way she does. But Jay — moments like these are beautiful because they’re real and rare. You’re not just seeing a pretty image — you’re feeling something deeper when you see her. That says a lot about how genuine your feelings are.

Just remember: admiring someone is lovely… but don't forget to admire yourself too. Because the guy who notices details like this, who feels deeply and honestly — that guy is worth being seen too.""")
    
with open("Notes.txt","r") as f:
    print(f.read())    

message=input("Enter your message: ")
with open("userlog.txt","w") as f:
    f.write(message)

with open("userlog.txt", "r") as f:
    print(f.read())    

for i in range(3):
    message=input(f"Enter line {i+1}\n")
    with open("userlog.txt","a") as f:
        f.write(f"\n{message}")

with open("userlog.txt","r") as f:
    lines=f.read() 
    print(lines) 