loginurl = "https://accounts.google.com/signin/v2/sl/pwd?passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fnext%3D%252F%26action_handle_signin%3Dtrue%26hl%3Den%26app%3Ddesktop&uilel=3&service=youtube&flowName=GlifWebSignIn&flowEntry=ServiceLogin"

with open('youtubedata.txt') as f:
    contents = f.read().split('\n')
    username = contents[0]
    password = contents[1]
    
print(username, password)
