ver=0.0
build=str(ver),".0"

def view_credits():
  print("2023 | E. \"Keklake-of-fire\" Keklak | CC-BY-SA\n\nVersion: ",ver,"\n\nBuild: ",build,"\n\n!!! WARNING: This software is not to be reverse-engineered for unethical or immoral purposes !!!")

def confirm_quit():
  x=input("Would you like to terminate the Wokemath program (Y + Enter)? ")
  if x="Y" or x="y": quit()
  else: continue

def wokify():
  # Not programmed lol #
  continue

def menu():
  x=input("You are viewing Wokemath's main menu:\n\nSubmit \"W\" to \"wokify\" your writing\n\nSubmit \"Q\" to Quit")
  if not(x="w" or x="w" or x="Q" or x="q"): menu()
  elif x="w" or x="w": wokify()
  else: confirm_quit()

def main():
  try:
    view_credits()
  except:
    print("Wokemath's credits did not load for some reason. Closing program automatically...")
    quit()
  except:
    quit()
  try:
    menu()
    continue
  except:
    print("Wokemath is having trouble running. Closing program automatically...")
    
quit()
